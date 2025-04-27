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

You are a resume section categorizer. Your task is to extract the **background** information from a resume and return it in clean JSON format. This includes contact and identity-related information that typically appears at the top of a resume or in the header.

Extract only the following fields if available:
- name
- location (city and state or ZIP)
- phone number
- email
- LinkedIn
- GitHub
- personal website or other relevant contact info

This section should not include education, experience, or summary/objective text. Your job is only to extract factual contact information that would appear in a resume header or footer.

Return the result in the following JSON format:
{
  "name": "John Doe",
  "location": "New York, NY",
  "phone": "123-456-7890",
  "email": "john.doe@example.com",
  "linkedin": "https://www.linkedin.com/in/john-doe",
  "github": "https://github.com/john-doe"
}

Only include fields that are explicitly present in the resume. Do not infer missing values.

Here is the rest of the resume:
"""


education_categorize_prompt = """

You are a resume section categorizer. Your task is to extract all **education-related** information and return it in clean JSON format. You are responsible for identifying any formal academic experiences, regardless of how they are labeled in the resume.

You should extract:
- school name
- degree
- major (if separate from degree)
- location (city, state)
- graduation date
- GPA
- coursework (if explicitly listed)

Do NOT include certifications, bootcamps, online courses, or professional training unless they are part of a degree program. Do NOT extract honors, awards, or scholarships unless they are part of an education entry.

Return the result in this JSON format:
{
  "education": {
    "School 1": {
      "school": "University of Example",
      "degree": "Bachelor of Science",
      "major": "Computer Science",
      "location": "Boston, MA",
      "graduation_date": "May 2024",
      "gpa": "3.85/4.00",
      "coursework": "Data Structures, Algorithms, Machine Learning"
    },
    "School 2": {
      ...
    }
  }
}

Only include fields that are clearly listed in the resume. Do not infer missing values or include unrelated training programs.

Here is the rest of the resume:
"""


experience_categorize_prompt = """

You are a resume section categorizer. Your task is to extract the **professional experience** section from a resume and return it in clean JSON format. Your responsibility includes identifying formal and informal work experiences such as internships, part-time jobs, freelance work, academic research roles, and project-based consulting.

You should extract entries that show:
- paid employment
- formal internships or apprenticeships
- professional or research roles, regardless of section header
- entrepreneurial or client-based consulting work

Each entry must include:
- role/title
- company or organization
- location
- date range or duration
- bullet points describing the work

Do NOT include extracurricular leadership positions, student clubs, volunteer work, or general projects. These will be handled by other categorization systems.

Return the result in this JSON format:
{
  "experience": {
    "Experience 1": {
      "role": "Software Engineering Intern",
      "company": "Google",
      "location": "Mountain View, CA",
      "duration": "June 2023 – August 2023",
      "bullet_point1": "...",
      "bullet_point2": "...",
      ...
    }
  }
}

Only include roles that clearly reflect professional experience. Do not make assumptions about jobs not clearly described.

Here is the rest of the resume:
"""



leadership_categorize_prompt = """

You are a resume section categorizer. Your task is to extract all **leadership and community engagement** experiences from the resume and return them in clean JSON format. These experiences may appear under headings like “Projects,” “Leadership,” “Involvement,” or not be labeled at all.

You should extract entries that involve:
- student organizations and leadership roles
- volunteer work or nonprofit service
- organizing community events or initiatives
- team-based projects with social or educational impact
- teaching, mentorship, or collaboration

You may include experiences even if they are unpaid or appear under a general “Projects” section — as long as the intent reflects leadership, teamwork, or community contribution.

Do NOT include professional internships, jobs, or client-based projects that are clearly experience-driven.

Return the result in this JSON format:
{
  "leadership_and_community": {
    "Engagement 1": {
      "organization": "Finance Club",
      "title": "Vice President",
      "location": "Atlanta, GA",
      "duration": "August 2022 – Present",
      "bullet_point1": "...",
      "bullet_point2": "...",
      ...
    }
  }
}

Only extract entries that clearly show initiative, collaboration, or public impact.

Here is the rest of the resume:
"""

honors_categorize_prompt = """

You are a resume section categorizer. Your task is to extract all **honors, awards, and recognitions** from the resume and return them in clean JSON format.

This includes:
- academic honors (e.g., Dean’s List, Latin honors)
- scholarships or merit-based awards
- athletic or leadership recognitions
- named institutional awards or titles
- professional acknowledgments

Do NOT include general experience or achievements unless they are explicitly labeled or written as awards.

Return the result in this JSON format:
{
  "honors": {
    "honor_1": "Dean’s List – Emory University (Fall 2021, Spring 2022)",
    "honor_2": "National Merit Scholar",
    "honor_3": "Varsity Soccer MVP 2023"
  }
}

Only include items that are clearly honors or awards. Skip anything ambiguous.

Here is the rest of the resume:
"""


skill_categorize_prompt = """

You are a resume section categorizer. Your task is to extract the **skills and interests** from a resume and return them in clean JSON format.

You should identify and organize the following categories:

- skills: technical or professional skills (e.g., software, programming languages, tools, methods)
- languages: language proficiencies (e.g., English – native, Spanish – fluent)
- interests: personal interests or hobbies (e.g., photography, soccer, gardening)

If the resume does not have an explicit skills section, infer likely skills based on the tools, technologies, and responsibilities mentioned in experience, education, or project sections. For example, if the candidate worked on “building dashboards in Tableau,” you should include Tableau in the skills list.

You are allowed to infer:
- programming languages or tools mentioned during professional or academic experience
- general categories like “data visualization” or “statistical analysis” if those activities are performed

Your goal is to generate a concise summary of the candidate’s demonstrated and implied skill set.

Return the result in the following JSON format:
{
  "skills": {
    "skills": "Python, SQL, Tableau, Excel",
    "languages": "Spanish (Fluent), Mandarin (Conversational)",
    "interests": "Hiking, Graphic Design, Chess"
  }
}

If any field is not clearly present or inferable from the resume, leave it out.

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

prompt_list = [background_categorize_prompt, education_categorize_prompt, experience_categorize_prompt, leadership_categorize_prompt, honors_categorize_prompt, skill_categorize_prompt]
    
if __name__ == "__main__":
    ocr_result = ocr("dat/alternative_styles/10554236.pdf")
    # response = categorize_prompt(prompt_list[5], ocr_result)
    # print(response)
    for section in prompt_list:
        response = categorize_prompt(section, ocr_result)
        print(response)
        time.sleep(2)
    # background_categorize_response = categorize_prompt(background_categorize_prompt, ocr_result)
    # print(background_categorize_response)
