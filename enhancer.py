from dotenv import load_dotenv
import google.generativeai as genai
from gemini_stem_categorizer import categorize_prompt
from gemini_stem_categorizer import experience_categorize_prompt as stem_experience
from gemini_business_categorizer import experience_categorize_prompt as business_experience

from gemini_stem_categorizer import background_categorize_prompt as stem_background
from gemini_stem_categorizer import involvement_categorize_prompt as stem_involvement
from gemini_stem_categorizer import projects_categorize_prompt as stem_projects

from resume_preprocess import ocr
import os

API_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_key)


experience_enhance_prompt = """
You are going to receive a json of the experience section of a a resume in a format that looks like:

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

I need you to improve the bullet_points such that we can maximize the potential of the user. 

I want you to take in the original description, then improve it using action verbs, and trying to implement quantitative information.
A format that is sometimes good to follow is Achieved [X] as measured by [Y] by doing [Z] and its variations. You do not have to always use this format, I am just giving it to you as a
guide. 

If they are missing a metric and having that metric would significantly improve the status of the description, make that bullet_point to what a sentence
might look like with the metric, and in place of the number put a place holder ie [put metric here] to indicate to the user to make that change accordingly. 

You can also try to infer what the user might have done in the job that they didn't write about, and create bullet points for that. 
However, IF YOU DO INFER, mark that it is inferred (follow the examples below). 

Here are some example inputs and outputs. I am going giving you the role and the bullet points (instead of the json file format that you would actually receive)

example input 1:
Software Engineer (Amazon):
- Contributed to the design and implementation of scalable backend services supporting high-traffic e-commerce applications.
- Led development of a cross-platform mobile application using React Native, enhancing user engagement across iOS and Android platforms.

example output for input 1:
- Achieved a [put metric here]% reduction in page load times by refactoring backend logic and optimizing database queries for high-traffic e-commerce services.
- Spearheaded development of a React Native app from wireframes to launch, resulting in [put metric here] active users and [put metric here]% increase in engagement.
- [inferred] Integrated third-party APIs and payment gateways, expanding product functionality and supporting [put metric here]% of user transactions without downtime. [inferred]
- [Inferred] Reduced deployment cycle time by [put metric here]% by working closely with DevOps to implement CI/CD pipelines using GitHub Actions

example input 2: 
Business Analyst (Deloitte)
- Worked closely with stakeholders to gather requirements and translate business needs into actionable insights and process improvements.
- Helped analyze survey data to increase satisfaction rates. 

example output for input 2:
- Transformed unstructured stakeholder feedback into clear functional requirements, enabling successful rollout of [put metric here] internal tools with minimal revisions.
- Achieved [put metric here]% improvement in customer satisfaction scores by identifying service pain points through survey analysis and proposing data-backed changes.
- [inferred] Built dynamic dashboards using Tableau to monitor KPIs across departments, increasing leadership visibility and decision-making speed. 
- [inferred] Collaborated with marketing to analyze A/B test results, providing insights that drove a [put metric here]% improvement in email campaign performance. 

example input 3:
Data Scientist (Spotify):
- Built predictive models using Python and scikit-learn to optimize marketing campaigns
- Designed and implemented data pipelines to automate reporting workflows, reducing manual effort

Example output for input 3:
- Built classification models using Python and scikit-learn that improved campaign targeting accuracy, achieving a [put metric here]% increase in lead conversion.
- Achieved a [put metric here] hour reduction in weekly reporting time by designing robust data pipelines in SQL and Pandas, automating manual workflows.
- [inferred] Conducted cohort analysis to uncover trends in user retention, directly informing product changes that boosted 30-day retention by [put metric here]%
- [inferred] Visualized key data trends using matplotlib and seaborn, enabling business teams to identify [put metric here]% increase in churn risk among specific user segments. 


Return in the same json format as the input, but you can increase the number of bullet points per role. 
HOWEVER, KEEP THE MAXIMUM NUMBER OF BULLET POINTS AT 5, this means that you should determine which bullet points are the best. Do not weigh the inferred one less than the other 
bullet points because it is inferred, but just look at the bullet points objectively. If you see that certain bullet points that the user gave are repetitive, feel free to combine. 
You can also add inferred material into a original bullet point to give it more life (and put the inferred from the point at which you started inferring)

If you get a section that doesn't look like it can be enhanced using these instructions, just return the original input json attached at the end. 

The output should OBJECTIVELY be better than the original information on the input resume. 
Now enhance the following input:

"""


def experience_enhancer(json_response_from_categorizer):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(experience_enhance_prompt + json_response_from_categorizer)
    return response.text

if __name__ == "__main__":
    path = "dat/alternative_styles/sasha_wagner.pdf"
    stem_exp = categorize_prompt(stem_experience, ocr(path))
    print(stem_exp)

    stem_back = categorize_prompt(stem_background, ocr(path))
    stem_inv = categorize_prompt(stem_involvement, ocr(path))
    stem_proj = categorize_prompt(stem_projects, ocr(path))

    stem_exp_enhanced = experience_enhancer(stem_exp)
    stem_back_enhanced = experience_enhancer(stem_back)
    stem_inv_enhanced =experience_enhancer(stem_inv)
    stem_proj_enhanced = experience_enhancer(stem_proj)

    print(stem_exp_enhanced)
    print(stem_back_enhanced)
    print(stem_inv_enhanced)
    print(stem_proj_enhanced)
