
from resume_preprocess import ocr
from gemini_stem_categorizer import clean_json_string, categorize_prompt

import os
from enum import Enum
from io import BytesIO
import tempfile


from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any
import json

import enhancer


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResumeRequest(BaseModel):
    section_type: str
    resume_text: Optional[str] = None
    file_path:Optional[str] = None

import gemini_business_categorizer
BUSINESS_SECTION_PROMPTS = {"background": gemini_business_categorizer.background_categorize_prompt ,
                            "education": gemini_business_categorizer.education_categorize_prompt,
                            "experience": gemini_business_categorizer.experience_categorize_prompt,
                            "leadership":gemini_business_categorizer.leadership_categorize_prompt,
                            "honors": gemini_business_categorizer.honors_categorize_prompt,
                            "skills":gemini_business_categorizer.skill_categorize_prompt

}
import gemini_stem_categorizer
STEM_SECTION_PROMPTS = {"background":gemini_stem_categorizer.background_categorize_prompt,
                        "education":gemini_stem_categorizer.education_categorize_prompt,
                        "experience":gemini_stem_categorizer.experience_categorize_prompt,
                        "skills":gemini_stem_categorizer.skills_categorize_prompt,
                        "projects":gemini_stem_categorizer.projects_categorize_prompt,
                        "involvement":gemini_stem_categorizer.involvement_categorize_prompt
                        }


def extract_json_from_response(response_text):
    cleaned_text = clean_json_string(response_text)
    try:
        return json.loads(cleaned_text)
    except json.JSONDecodeError:
        try: 
            start_idx = cleaned_text.find('{')
            end_idx = cleaned_text.find('}')
            if start_idx != -1 and end_idx != 0:
                json_str = cleaned_text[start_idex:end_idx]
                return json.loads(json_str)
        except:
            raise Exception("Failed to extract valid JSON from response")
        

@app.post('/categorize_section_business_string')
async def categorize_business(request:ResumeRequest):
    # validating section types
    if request.section_type not in BUSINESS_SECTION_PROMPTS:
        raise HTTPException(status_code=400, detail=f"Invalid section type. Available types: {list(BUSINESS_SECTION_PROMPTS.keys())}")
    resume_text = ""
    if request.resume_text:
        resume_text = request.resume_text
    elif request.file_path:
        try:
            resume_text = ocr(request.file_path)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"OCR processing error: {str(e)}")
    else:
        raise HTTPException(status_code=400, detail="Either resume_text or file_path must be provided")
    
    
    prompt = BUSINESS_SECTION_PROMPTS[request.section_type] 
    try:
        result = categorize_prompt(prompt,resume_text)
        json_result = extract_json_from_response(result)
        return {
            "section_type": request.section_type,
            "result": json_result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "Resume Processing API is running. See /docs for API documentation."}

@app.post("/categorize_business/upload")
async def categorize_business_resume_upload(file: UploadFile = File(...),section_type: str = Form(...)):
    if section_type not in BUSINESS_SECTION_PROMPTS:
        raise HTTPException(status_code=400, 
                          detail=f"Invalid section type. Available types: {list(BUSINESS_SECTION_PROMPTS.keys())}")
    try:
        temp_file_path = f"temp_{file.filename}"
        with open(temp_file_path, "wb") as buffer:
            buffer.write(await file.read())

        resume_text = ocr(temp_file_path)
        
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
        
        prompt = BUSINESS_SECTION_PROMPTS[section_type]
        
        result = categorize_prompt(prompt, resume_text)
        
        json_result = extract_json_from_response(result)
        return {
            "section_type": section_type,
            "result": json_result
        }
    except Exception as e:
        if 'temp_file_path' in locals() and os.path.exists(temp_file_path):
            os.remove(temp_file_path)
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/categorize_section_stem_string')
async def categorize_business(request:ResumeRequest):
    # validating section types
    if request.section_type not in STEM_SECTION_PROMPTS:
        raise HTTPException(status_code=400, detail=f"Invalid section type. Available types: {list(STEM_SECTION_PROMPTS.keys())}")
    resume_text = ""
    if request.resume_text:
        resume_text = request.resume_text
    elif request.file_path:
        try:
            resume_text = ocr(request.file_path)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"OCR processing error: {str(e)}")
    else:
        raise HTTPException(status_code=400, detail="Either resume_text or file_path must be provided")
    
    
    prompt = STEM_SECTION_PROMPTS[request.section_type] 
    try:
        result = categorize_prompt(prompt,resume_text)
        json_result = extract_json_from_response(result)
        return {
            "section_type": request.section_type,
            "result": json_result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/categorize_stem/upload")
async def categorize_business_resume_upload(file: UploadFile = File(...),section_type: str = Form(...)):
    if section_type not in STEM_SECTION_PROMPTS:
        raise HTTPException(status_code=400, 
                          detail=f"Invalid section type. Available types: {list(STEM_SECTION_PROMPTS.keys())}")
    try:
        temp_file_path = f"temp_{file.filename}"
        with open(temp_file_path, "wb") as buffer:
            buffer.write(await file.read())

        resume_text = ocr(temp_file_path)
        
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
        
        prompt = STEM_SECTION_PROMPTS[section_type]
        
        result = categorize_prompt(prompt, resume_text)
        
        json_result = extract_json_from_response(result)
        return {
            "section_type": section_type,
            "result": json_result
        }
    except Exception as e:
        if 'temp_file_path' in locals() and os.path.exists(temp_file_path):
            os.remove(temp_file_path)
        raise HTTPException(status_code=500, detail=str(e))


class EnhancerRequest(BaseModel):
    categorized_json: Dict[str, Any]

@app.post("/enhance/experience")
async def enhance_experience(request: EnhancerRequest):
    try:
        # Convert the input JSON to a string
        json_str = json.dumps(request.categorized_json)
        
        # Process through your enhancer
        enhanced_result = enhancer.experience_enhancer(json_str)
        
        # Clean and parse the response
        try:
            # Use your existing clean_json_string function if the response comes back in code blocks
            cleaned_response = clean_json_string(enhanced_result)
            
            # Try to parse as JSON
            try:
                json_result = json.loads(cleaned_response)
                return {
                    "status": "success",
                    "enhanced_result": json_result
                }
            except json.JSONDecodeError:
                return {
                    "status": "success",
                    "enhanced_result": cleaned_response,
                    "format": "text"  # Indicate this is text, not JSON
                }
        except Exception as e:
            return {
                "status": "success",
                "enhanced_result": enhanced_result,
                "format": "text"
            }
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error enhancing experience: {str(e)}")