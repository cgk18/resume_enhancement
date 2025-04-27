# Resume Processing API - Frontend Integration Guide

This guide explains how to integrate your frontend application with our Resume Processing API.

## Overview

The Resume Processing API analyzes resume content, categorizes different sections, and enhances professional experiences. It's designed to work with both business and STEM resumes, supporting both direct text input and file uploads.

## Quick Start

### Base URL

```
http://127.0.0.1:8000/docs
```

## API Endpoints

### Business Resume Processing

#### Categorize Business Resume Section (Text Input)
```
POST /categorize_section_business_string
```
Request body:
```json
{
  "section_type": "experience",
  "resume_text": "Your resume section text here..."
}
```

#### Categorize Business Resume Section (File Upload)
```
POST /categorize_business/upload
```
Form data:
- `file`: The resume file to upload (PDF, DOCX, etc.)
- `section_type`: The type of section to categorize

Available business section types:
- `background` - General background information
- `education` - Academic history
- `experience` - Work experience
- `leadership` - Leadership roles and achievements
- `honors` - Awards and recognitions
- `skills` - Professional skills and competencies

### STEM Resume Processing

#### Categorize STEM Resume Section (Text Input)
```
POST /categorize_section_stem_string
```
Request body:
```json
{
  "section_type": "experience",
  "resume_text": "Your resume section text here..."
}
```

#### Categorize STEM Resume Section (File Upload)
```
POST /categorize_stem/upload
```
Form data:
- `file`: The resume file to upload (PDF, DOCX, etc.)
- `section_type`: The type of section to categorize

Available STEM section types:
- `background` - General background information
- `education` - Academic history
- `experience` - Work experience
- `skills` - Technical skills and competencies
- `projects` - Technical/research projects
- `involvement` - Professional involvement and activities

### Experience Enhancement

Improves the quality and impact of experience descriptions by rephrasing and enhancing the content.

```
POST /enhance/experience
```
Request body:
```json
{
  "categorized_json": {
    "experience": {
      "Experience 1": {
        "role": "Software Engineering Intern",
        "company": "Google",
        "location": "Mountain View, CA",
        "duration": "June 2023 – August 2023",
        "bullet_point1": "Developed a new feature for Google Maps",
        "bullet_point2": "Fixed bugs in the existing codebase",
        "bullet_point3": "Participated in code reviews"
      }
    }
  }
}
```

## Integration Examples

### React Example

```javascript
// Resume Section Categorization
const categorizeResumeSection = async (sectionType, resumeText) => {
  try {
    const response = await fetch('https://your-api-domain.com/categorize_section_business_string', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        section_type: sectionType,
        resume_text: resumeText
      }),
    });
    
    if (!response.ok) {
      throw new Error('API request failed');
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error categorizing resume section:', error);
    throw error;
  }
};

// File Upload Example
const uploadResumeFile = async (file, sectionType) => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('section_type', sectionType);
  
  try {
    const response = await fetch('https://your-api-domain.com/categorize_business/upload', {
      method: 'POST',
      body: formData,
    });
    
    if (!response.ok) {
      throw new Error('File upload failed');
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error uploading resume:', error);
    throw error;
  }
};

// Experience Enhancement
const enhanceExperience = async (categorizedJson) => {
  try {
    const response = await fetch('https://your-api-domain.com/enhance/experience', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        categorized_json: categorizedJson
      }),
    });
    
    if (!response.ok) {
      throw new Error('Enhancement request failed');
    }
    
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error enhancing experience:', error);
    throw error;
  }
};
```

### Complete Integration Flow Example

```javascript
import React, { useState } from 'react';

function ResumeProcessor() {
  const [file, setFile] = useState(null);
  const [sectionType, setSectionType] = useState('experience');
  const [resumeType, setResumeType] = useState('business'); // 'business' or 'stem'
  const [results, setResults] = useState(null);
  const [enhanced, setEnhanced] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      // Create form data
      const formData = new FormData();
      formData.append('file', file);
      formData.append('section_type', sectionType);
      
      // Determine endpoint based on resume type
      const endpoint = resumeType === 'business' 
        ? 'https://your-api-domain.com/categorize_business/upload'
        : 'https://your-api-domain.com/categorize_stem/upload';
      
      // Upload and categorize the resume
      const response = await fetch(endpoint, {
        method: 'POST',
        body: formData,
      });
      
      if (!response.ok) {
        throw new Error('Failed to process resume');
      }
      
      const data = await response.json();
      setResults(data);
      
      // If this is experience data, we can enhance it
      if (sectionType === 'experience') {
        const enhanceResponse = await fetch('https://your-api-domain.com/enhance/experience', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            categorized_json: data.result
          }),
        });
        
        if (enhanceResponse.ok) {
          const enhancedData = await enhanceResponse.json();
          setEnhanced(enhancedData);
        }
      }
    } catch (error) {
      console.error('Error processing resume:', error);
      alert('Failed to process resume: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="resume-processor">
      <h2>Resume Section Processor</h2>
      
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            Resume Type:
            <select 
              value={resumeType} 
              onChange={(e) => setResumeType(e.target.value)}
            >
              <option value="business">Business</option>
              <option value="stem">STEM</option>
            </select>
          </label>
        </div>
        
        <div>
          <label>
            Section Type:
            <select 
              value={sectionType} 
              onChange={(e) => setSectionType(e.target.value)}
            >
              {resumeType === 'business' ? (
                <>
                  <option value="background">Background</option>
                  <option value="education">Education</option>
                  <option value="experience">Experience</option>
                  <option value="leadership">Leadership</option>
                  <option value="honors">Honors</option>
                  <option value="skills">Skills</option>
                </>
              ) : (
                <>
                  <option value="background">Background</option>
                  <option value="education">Education</option>
                  <option value="experience">Experience</option>
                  <option value="skills">Skills</option>
                  <option value="projects">Projects</option>
                  <option value="involvement">Involvement</option>
                </>
              )}
            </select>
          </label>
        </div>
        
        <div>
          <label>
            Resume File:
            <input 
              type="file" 
              accept=".pdf,.docx,.doc" 
              onChange={handleFileChange}
              required
            />
          </label>
        </div>
        
        <button type="submit" disabled={loading || !file}>
          {loading ? 'Processing...' : 'Process Resume'}
        </button>
      </form>
      
      {results && (
        <div className="results">
          <h3>Categorized Results:</h3>
          <pre>{JSON.stringify(results, null, 2)}</pre>
          
          {enhanced && (
            <>
              <h3>Enhanced Experience:</h3>
              <pre>{JSON.stringify(enhanced, null, 2)}</pre>
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default ResumeProcessor;
```

## Response Formats

### Categorization Response Example

```json
{
  "section_type": "experience",
  "result": {
    "experience": {
      "Experience 1": {
        "role": "Software Engineering Intern",
        "company": "Google",
        "location": "Mountain View, CA",
        "duration": "June 2023 – August 2023",
        "bullet_point1": "Developed a new feature for Google Maps",
        "bullet_point2": "Fixed bugs in the existing codebase",
        "bullet_point3": "Participated in code reviews"
      }
    }
  }
}
```

### Enhancement Response Example

```json
{
  "status": "success",
  "enhanced_result": {
    "experience": {
      "Experience 1": {
        "role": "Software Engineering Intern",
        "company": "Google",
        "location": "Mountain View, CA",
        "duration": "June 2023 – August 2023",
        "bullet_point1": "Developed and deployed a new feature for Google Maps used by [put metric here] daily active users, improving [put impact here, e.g., route accuracy, user navigation experience].",
      "bullet_point2": "Resolved [put metric here] high-priority bugs in the legacy codebase by conducting root cause analysis, enhancing system stability and performance.",
      "bullet_point3": "Participated in cross-functional code reviews, identifying [put metric here] potential issues and contributing to higher code quality and maintainability.",
      "bullet_point4": "[inferred] Collaborated with UX designers and product managers to refine user workflows, helping reduce user drop-off rates by [put metric here]%.",
      "bullet_point5": "[inferred] Wrote unit and integration tests for new and existing features, increasing test coverage by [put metric here]% and reducing post-deployment issues."
      }
    }
  }
}
```

## Error Handling

The API returns standard HTTP status codes:

- `200 OK`: Request successful
- `400 Bad Request`: Invalid input (e.g., missing fields or invalid section type)
- `500 Internal Server Error`: Server-side error

Error response format:
```json
{
  "detail": "Error message describing what went wrong"
}
```

## Best Practices

1. **File Handling**: Limit uploads to PDF formats
2. **Error Handling**: Implement proper error handling in your frontend application
3. **Loading States**: Show loading indicators during API calls, as processing may take several seconds
4. **Validation**: Validate section types before making API calls
5. **Progressive Enhancement**: Show categorized results first, then enhanced results when available

## Support

For questions or issues, contact the backend team at [support-email].
