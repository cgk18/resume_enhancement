import json
from dotenv import load_dotenv
import google.generativeai as genai
import os
from resume_preprocess import ocr
import time

load_dotenv()

API_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_key)

def categorize_prompt(prompt, ocr_result):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt + ocr_result)
    return response.text

background_categorize_prompt = """

You are a resume section categorizer. Your task is to extract the **background** information from resumes and return it in clean JSON format. The background section should contain the following fields, if available:

- name  
- location  
- phone  
- email  
- linkedin  
- github 

Return the JSON in the following format:
{
    "name": "Student Name",
    "location": "Atlanta, GA",
    "phone": "915-232-5578",
    "email": "first.last@emory.edu",
    "linkedin": "linkedin.com/in/firstnamelastname",
    "github": "github.com/student"
}

Only use the information explicitly present in the resume. Do not infer or guess any missing values.

Here is the rest of the resume:
"""

description_categorize_prompt = """

You are a resume section categorizer. Your task is to extract or generate a concise and well-written professional summary for a software engineering resume. This is often labeled as a "Professional Summary," "Profile," "Career Objective," or appears under the candidate's name and title.

Your output should be a short paragraph (2–5 sentences) that introduces the candidate, highlights their areas of expertise, and conveys enthusiasm and readiness for a software engineering role.

If a summary or statement is already present, extract and lightly clean it.

If no summary exists, infer and generate one based on the resume’s information, such as:
- technical skills and tools used
- types of projects completed
- industry exposure (e.g. internships, teams, clients)
- soft skills (e.g. collaboration, communication, problem-solving)

Return the output in this JSON format:
{
    "description": "Motivated and detail-oriented aspiring software engineer with a strong foundation in full-stack development and a passion for problem-solving. Eager to apply technical skills in programming, software design, and project collaboration to contribute to innovative projects."
}

Only generate content that could reasonably be written by the candidate based on their resume. Do not exaggerate or fabricate experience.

Here is the rest of the resume:
"""


education_categorize_prompt = """

You are a resume section categorizer. Your task is to extract the **education** section from a software engineering resume and return it in clean JSON format.

You should extract:
- school  
- degree  
- location  
- graduation_date

This section only includes formal academic programs (e.g., bachelor’s degree). Do NOT include bootcamps, certifications, or training courses — those will be handled by another categorizer if applicable.

Return the JSON in the following format:
{
    "education": {
        "School 1": {
            "school": "Emory University",
            "degree": "Bachelor of Science in Computer Science",
            "location": "Atlanta, GA",
            "graduation_date": "May 2026"
        }
    }
}

Only include fields that are explicitly stated. Do not infer any missing fields.

Here is the rest of the resume:
"""


skills_categorize_prompt = """

You are a resume section categorizer. Your task is to extract the **core competencies and technical skills** section from a software engineering resume and return it in clean JSON format.

This section includes two main categories:
- core_competencies: high-level skill areas or domains (e.g., Debugging, Algorithms, UI Design)
- technical_skills: programming languages, tools, and technologies (e.g., Python, SQL, React)

You may also infer additional skills from the projects or experience section, as long as they clearly demonstrate regular usage.

Return the JSON in the following format:
{
    "skills": {
        "core_competencies": "Debugging & Testing, Data Structures & Algorithms, Front-End, Back-End, User Experience, Artificial Intelligence",
        "technical_skills": "Python, SQL, Excel, R"
    }
}

Only include what is present or strongly inferable from the resume.

Here is the rest of the resume:
"""


projects_categorize_prompt = """

You are a resume section categorizer. Your task is to extract the **technical projects** section from a software engineering resume and return it in clean JSON format.

You should extract:
- project_name  
- technologies used  
- github_link or external URL (if present)  
- up to 3 bullet points describing purpose, outcome, or implementation

This section only includes self-initiated or team-based software projects. Do NOT include internships, jobs, or club roles — those go in Experience or Involvement.

Return the JSON in the following format:
{
    "projects": {
        "Project 1": {
            "project_name": "Smart Recipe Recommender",
            "technologies": "React, Flask, MongoDB",
            "github": "github.com/student/project",
            "description1": "Built a web app that recommends recipes based on user preferences and ingredients",
            "description2": "Implemented authentication and RESTful API endpoints",
            "description3": "Deployed using Heroku and tested with Cypress"
        }
    }
}

Only include content that reflects student or independent technical builds.

Here is the rest of the resume:
"""

experience_categorize_prompt = """

You are a resume section categorizer. Your task is to extract the **experience** section from a software engineering resume and return it in clean JSON format.

This includes internships, freelance work, paid employment, or contract roles.

For each role, extract:
- title  
- company  
- duration  
- location (if shown)  
- up to 5 bullet points summarizing the impact or responsibilities

Do NOT include technical projects or club roles — those go under “Technical Projects” or “Involvement & Engagement.”

Return the JSON in the following format:
{
    "experience": {
        "Experience 1": {
            "role": "Software Engineer Intern",
            "company": "Tech Company LLC",
            "location": "Remote",
            "duration": "Summer 2023",
            "bullet_point1": "Built RESTful APIs and integrated with a front-end app using React",
            "bullet_point2": "Reduced page load time by 30% through caching optimizations",
            "bullet_point3": "Deployed CI/CD pipeline with GitHub Actions"
        }
    }
}

Here is the rest of the resume:
"""


involvement_categorize_prompt = """

You are a resume section categorizer. Your task is to extract the **involvement and engagement** section from a software engineering resume and return it in clean JSON format.

This includes student organizations, volunteer work, club memberships, and campus leadership.

Do NOT include internships or technical projects — those are categorized elsewhere.

Return the JSON in the following format:
{
    "involvement": {
        "involvement_1": "Vice President, Data Club",
        "involvement_2": "Member, Women in STEM",
        "involvement_3": "Volunteer, Second Harvest"
    }
}

Only include entries that reflect collaboration, leadership, or service.

Here is the rest of the resume:
"""


def clean_json_string(s):
    s = s.strip()
    if s.startswith("```"):
        lines = s.splitlines()
        if lines[0].strip().startswith("```"):
            lines = lines[1:]

        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]
        s = "\n".join(lines).strip()
    return s

prompt_list = [background_categorize_prompt, description_categorize_prompt, education_categorize_prompt, skills_categorize_prompt, projects_categorize_prompt, experience_categorize_prompt, involvement_categorize_prompt]
    
if __name__ == "__main__":
    ocr_result = ocr("dat/alternative_styles/sasha_wagner.pdf")
    for section in prompt_list:
        response = categorize_prompt(section, ocr_result)
        print(response)
        time.sleep(2)
    # background_categorize_response = categorize_prompt(background_categorize_prompt, ocr_result)
    # print(background_categorize_response)
