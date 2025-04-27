from openai import OpenAI
import resume_preprocess
import json
from dotenv import load_dotenv


client = OpenAI(api_key=API_key)

client.api_key = API_key

sasha_ocr_result = """
SASHA WAGNER

DIGITAL MARKETING ANALYST

CONTACT

sashawagner@email.com
(123) 456-7890

Saint Paul, MN

LinkedIn

EDUCATION

B.S. in Marketing
University of St. Thomas
August 2018 - May 2022
(anticipated)

Saint Paul, MN

GPA: 3.65

RELEVANT
COURSES

Intro to Marketing
Marketing Research
Consumer Behavior

SalesForce Management
Electronic Commerce

Advertising and Sales
Promotion

Principles of Selling

SKILLS

Salesforce

Microsoft Excel, Word,
Powerpoint

Paid acquisition (Facebook,
Google, LinkedIn, Instagram,
retargeting)

Google Analytics

SEO

CAREER OBJECTIVE

Soon-to-be marketing graduate (2022) with a passion for developing
scalable acquisition strategies through paid advertising and SEO. |
have experience creating and improving campaigns in the context of
a big team, and | worked independently to help local organizations
start and grow user acquisition, skills that will positively impact
strategic development and execution at Pacsun.

WORK EXPERIENCE

Digital Marketing Analyst Intern
Marketing Science Associates
April 2021 - current / Saint Paul, MN
+ Created A/B testing plan for Facebook ad copy, leading to an
improvement in ROI of 18%
* Built key reports for executive team around KPIs, such as
marketing spend, new leads, revenue generated, and ROI
* Oversaw the creation of the blog for SEO purposes, which grew
from 500 to 5,000 monthly organic visitors
+ Interviewed clients to understand their product positioning to
incorporate into ad copy, resulting in client satisfaction of 96%

* Designed weekly email campaigns to target potential
subscribers, increasing subscriptions by 12%

* Gathered data and insights, and discussed trends with team of 3
other interns and 4 analysts to set new goals

PROJECTS
Local SEO boost

* Helped local boutiques grow their online presence, boosting
their organic search traffic by an average of 60%

* Instructed clients in best SEO practices to see an average
increase in sales from online channels of $2.5K per month after
implementation

Paid ads for animal shelter
* Partnered with local animal shelter to build a paid advertising
campaign on Facebook and Instagram, resulting in a reduction
in cost per lead of 53%
* Iterated on ad copy, placement, and images to ultimately
improve conversion rate by 134%

"""

""" TEST IF THE MATERIAL WORKS BASIC CODE TO SEE IF THE MATERIAL RUNS

response = client.responses.create(
    model = "gpt-3.5-turbo",
    input = prompt + ocr_result
)

print(response.output_text)"""

accountant_ocr_result = """Summary

Financial Accountant specializing in financial planning, reporting and analysis within the Department of Defense.

Highlights
e Account reconciliations
e Results-oriented e Accounting operations professional
e Fimancial reporting e Analysis of financial systems
¢ Critical thinking e ERP (Enterprise Resource Planning) software.
e Excellent facilitator
Accomplishments

Served on a tiger team which identified and resolved General Ledger postings in DEAMS totaling $360B in accounting adjustments. This allowed
for the first successful fiscal year-end close for 2012.

In collaboration with DFAS Europe, developed an automated tool that identified duplicate obligations. This tool allowed HQ USAFE to
deobligate over $5M in duplicate obligations.

Experience
Company Name July 2011 to November 2012 Accountant

City ,

State

Enterprise Resource Planning Office (ERO)

In this position as an Accountant assigned to the Defense Enterprise Accounting and Management System (DEAMS) ERO I was
responsible for identifying and resolving issues affecting the DEAMS General Ledger.

I worked with teammates from the Procure to Pay, Orders to Cash, and Budget to Report areas to resolve daily challenges encountered
with the deployment of DEAMS to additional customers and when system change requests were promoted to production.

I supported the testing of scripts, patches, and system change requests ensuring any anomalies were Wentified to the DEAMS Functional
Management Office for action by the DEAMS Program Management Office and/or the System Integrator.

In addition, I served on a tiger team designed to identify and resolve General Ledger posting differences and supported the development of
$360B in accounting adjustments allowing for the first successful fiscal year-end close in 2012.

These actions also allowed for the reconcihation and closure of fiscal year 2010 and 2011 accounting adjustments ensuring that all DEAMS
fiscal year-end requirements were completed.

These actions were recognized as critical to the successful review report issued by the Air Force Operational Test and Evaluation Center
(AFOTEC) resulting in the Air Force recetving the authority to continue with the deployment of DEAMS.

Company Name April 2010 to June 2011 Resource Advisor

City ,

State

In this position as Resource Advisor for the 1st Air Communications Operation Squadron (1 ACOS) I was responsible for providing
financial advice and decision support to the Commander.

I was responsible for coordinating a $4.6M budget between four finding sources.

I coordinated with USAFE Directorate of Intelligence (USAFE/A2), USAFE Directorate of Air and Space Operations (USAFE/A3),
USAFE Directorate of Communications (USAFE/A6) and the 435th Air Ground Operations Wing to ensure 1ACOS meets its mission
requirements.

I consistently managed three separate timelines for providing budget/unfunded requirements, providing documentation and various reports in
the required format for each organization.

I discussed the outcome of the Group and Directorate budget meetings providing feedback the same day to the Flight Chief§ and CC any
issue which affects 1ACOS directly.

I monitored the Defense Travel System (DTS) daily and identify orders and authorizations needing approval and provided notification to the
appropriate Reviewing Officials and Approvers.

Utilizmg DTS and the General Accounting and Finance System I reviewed status reports to identify anomalies in obligations and have
identified those orders which require correction prior to payment.

I provided Government Purchase Card (GPC) status reports the same day they are requested and in addition, communicated with the
appropriate cardholders when changes were required to support their program.

1 identified cardholder trammg requirements and monitored these requirements to ensure all required training was completed in support of
this mission critical program.

I developed guidance for the GPC cardholders on procedures for requesting training for the squadron and in addition | provided answers to
cardholder questions on unique or nonstandard issues/concerns.

e Assumed the role of the Billing Official during my final rating period and completed a self inspection of the program for the Management

Control Program, zero findings.
© Dung yearly audit by 700th CONS received zero findings.

Company Name July 2008 to April 2010 Staff Accountant
City , State

e Inmy position as the Staff Accountant for HQ USAFE I was responsible for providing accounting and financial oversight and advice to
customers throughout the Command in support of the USAFE Comptroller.

e | was responsible for performmng ongoing analysis of financial programs to identify negative trends and weaknesses, ensured specific
weaknesses were corrected, and determmed whether systemic or repeat issues were identified and adequately addressed.

e | was required to apply a comprehensive knowledge of analysis/reporting requirements and data produced to resolve these issues.

e Incollaboration with DFAS Europe, developed an autormted tool that identifies duplicate obligations by comparing records in the
accounting system to the contracting system and provided notification to the funds manager for review and resolution.

¢ This tool eliminated hours of manual research and results allowed HQ USAFE to deobligate over $5M in duplicate obligations.

e | was responsible for establishing various performance metrics which ensured effective and efficient use of USAFE financial resources.

e Isupported the USAFE/FMA Financial metrics program by collaborating with DFAS Limestone in the development of an automated tool
that provided senior leaders with visibility to any USAFE unit that is not in compliance with the established rules and regulations related to
the GPC.

e This tool provides management reports that are used to populate the monthly metric charts which are briefed by the USAFE/FMA.

e This tool provided the capability for USAFE/FMA to collaborate with USAFE Contracting and develop/deploy jomnt guidance that supports

the established Air Force Instruction mandating card suspension for card holders who are not in compliance with required reservation of
funds in the entitlement system in support of the GPC.

© | identified and resolved a problem with five GPC accounts that had been rejecting during the automated interface process each month.

e My research revealed that these accounts were rejecting for invalid paying station and required manual intervention by both Wing and
DFAS personnel.

e This not only created rework, it delayed the payment of the invoices.

e J partnered with DFAS Denver, corrected the records in the Access On-Line accounts elimmnating the error condition.

e | identified a method to deliver one-on-one trammng in support of the USAFE deployment of the Open Document Analysis (ODA) tool in
FMSutte.

e By utilizing Defense Connect Online I provided traming remotely, virtually elimmnating the need to expend funds on Temporary Duty (TDY)
travel.

e The results of this training produced results that went well above expectations and were noted by the ODA Program Management Office.

Company Name January 2007 to July 2009 Chief; Reports Branch. Accounts Maintenance and Control
City , State

e Inmy position as Chief ofthe Reports Branch in Accounts Maintenance & Control (AM&C) I was responsible for ensuring the
development and standardization of various managerial and system reports.

e | was responsible for the completeness and accuracy of weekly, monthly, quarterly, semi-annual, and annual reports.

e My branch monitored errors in the General Accounting and Finance System (GAFS/BQ) and ensured corrective actions were
accomplished.

e |also ensured fund balances were reconciled and reports were verified prior to release to base activities and higher headquarters.

e Limestone reorganized under the High Performing Organization (HPO) in January 2007 and at that time I was reassigned to AM&C, a
Directorate which previously did not exist.

e My challenge during that time was to staffmy branch, implement an aggressive trang schedule, and ensure the continuity of financial

reporting was maintained.

As we transitioned into the HPO we continued defining the missions and functions for AM&C for the entire network.

I participated in biweekly conference calls with Standards and Compliance in an effort to define missions and functions for AM&C.

Worked with management in determining FTEs needed for the branch,

I was responsible for developing meanngful performance standards for my employees since this branch and its functions did not previously

exist,

e Limestone POC for an initiative to eliminate suspense accounts throughout the agency.

e Identified suspense accounts not mitially targeted, formulated strategies to eliminate accounts or requested waivers, and participated in plans

to modify processes using suspense accounts, such as the interfiind suspense account.

e These actions provided initial progress towards meeting the Department of Treasury's mandate to discontinue suspense accounts by
February 2009.

¢ Worked with staffto reduce reconciliations from $6.9 million in February 2007 to $1.1 million in August, accomplished this despite loss in
experienced personnel and realignng resources to support critical mitiatives in Accounts Payable.

¢ | orchestrated the transition of reporting requirements for the Transportation Financial Management System (TFMS) workload ftom DFAS

Onnuha to Limestone.
e After transition to Limestone encouraged staffresponsible for these reports to streamline the processes.

¢ Staffautonmted a completely manual, time consuming process, thus elimmating potential key stroke errors and manually validating numerous

spreadsheets and listings.
© Contributor to Federal Managers Financial Integrity Act (FMFIA) Compliance Review and establishment of assessable units.

Identified inconsistencies mn information provided by staff on foreign currency fluctuation adjustments.
Persisted in getting higher level review of regulatory and policy guidance.
Report of foreign currency fluctuation is now consistently accurate.

Company Name February 2000 to January 2007 Chief, Accounts Payable Branch

City ,

State

As Chief Of Accounts Payable I was responsible for the overall management ofa branch consisting of over 120 employees.

My four first Ine supervisors were responsible for establishing priorities, schedules, and work assignments ensurmg changes in workload are
accounted for to mmimize the impact on normal office operations.

We consistently reviewed these areas and made necessary personnel moves based on shifting priorities.

This was extremely important during the DFAS Denver directed database consolidations and with the assumption of the Air National Guard
workload.

Workload increased rapidly while staffing increased gradually, which dictated frequent priority changes and personnel moves.

I also worked closely with the Major Commands supported by DFAS Limestone strengthening our partnership when workload spikes
negatively impacted our customers.

In December 2004, our overaged invoice percentage was nearing 25% and we had a backlog of vendor pay documents exceeding 30,000.
By working with the DFAS Command Client Executives and the Major Command Comptrollers, I was instrumental in forming a strategy
that included soliciting Air Force personnel assistance in document processing, identification of "must pay now" bills, and the formation of
special action response teams dedicated to responding to our customer's most urgent requirements.

As a result of these efforts, in a three month period, we were able to reduce our overaged invoice percentage by 19% and our backlog of
documents to no documents over 20 days old thereby minimizing the adverse impact on customer funds.

I was responsible for providing personnel feedback sessions quarterly and prepared supervisory appraisals of employees’ performance and
potential for advancement.

Partnering with the management staff and employees, I was instrumental in establishing Employee Performance Plans that linked employee
performance to established DFAS Strategies and Balance Scorecard goals.

In this position as a supervisory accountant I was responsible for performing ongoing analysis of the Vendor Pay workflow and production
to identify negative trends and weaknesses, ensure specific weaknesses have been corrected, and determmne whether systemic or repeat
issues have been identified and adequately addressed.

I was required to apply a comprehensive knowledge of analysis/reportmg requirements, work processes, vendor pay system structures, and
data produced to resolve these issues.

Utilizing my expertise with Louis II data retrieval software, | produced ad-hoc data queries for in-house and external use by our customers.
These retrievals were designed to reduce the man- hours necessary to perform complex finance and accounting functions by DFAS and Air
Force personnel.

I was responsible for the budget resources necessary to operate the branch.

In this capacity, I prepared budget over execution justifications, plan and monitor overtime costs, and control supply purchases to ensure the
most cost efficient operation possible.

I was required to respond to inquiries from various sources, which include, but are not limited to, vendors, DFAS management, accounting
liaison offices, resource advisors, and other DFAS field sites.

These inquiries required my ability to relay technical aspects of systems deficiencies to customers who are not familiar with our operation.

I participated in video teleconferences, conference calls, and briefings designed to address customer and DFAS management requirements.
I was called upon to explam, in laymen's terms, DFAS policy and procedures with regards to delays in payment due to various reasons.

I responded to various audit reports and studies; ensuring senior management and audit personnel, understand particular situations within the
Vendor Pay business process that result in these findings.

Company Name February 1999 to February 2000 Chief, Recon and Reports Branch

City ,

State

In ny position as Chief} Vendor Pay Reports and Recon Branch, I exercised supervision (either directly or indirectly) over 22 employees
prinurily in the "525" series in grades ranging from GS-5 through GS-8.

This responsibility also included supervision of the German local national workers assigned to my duty section.

I was responsible for planning, directing, and supervising the activities of the work force in the review, interpretation, processing, and
reconciliation of vendor pay and accounting data and the production of timely and accurate financial statement report requirements.

I participated in the development of branch policies continually reviewing and evaluating the organizational operations, work distribution, and
procedures.

I coordinated the activities of the assigned functions with those of other organizations to obtain the most effective correlation of financial
data.

Directed and provided technical guidance to subordinates in the assigned area.

Assured the timeliness and accuracy of assigned workload.

Planned, organized, directed, coordinated, and reviewed the work of subordinate's sections ensuring the mission and functions of the
division were carried out.

I managed and realigned resources, conducted program analyses, and made decisions in accordance with unit cost principles, outputs,
targets, and changing budgetary constramts.

I participated in long range planning, goal setting, and evaluating the subordinate staff.

Interpreted and clarified branch policies and resolved operational problems.

Ensured efficient utilization and professional development of my staff.

I was expected to provide reasonable assurance that operations were conducted in compliance with applicable laws and that funds,
property, and other assets were safeguarded against waste, loss, unauthorized use, or misappropriation.

I ensured contmuing and affirmative application and support of DoD and DFAS policy concerning the equal opportunity and affirmative
action programs.

Ensured personnel management within organizational entity under my supervision was accomplished without regard to race, color, religion,
sex, age, national origm, or handicap.

I kept abreast of developments, policy issuance, and other similar material in the equal opportunity field and fully supported the DoD and
DFAS Equal Opportunity Program.

I was responsible and accountable for the safety and health of my subordinates.

1 ensured personnel were trained to work safely.

I enforced safety and health rules, corrected unsafe or unhealthy acts and unsafe or unhealthy mechanical or physical conditions, investigated
mishaps and tool other actions necessary to ensure the safety and health of my employees.

Company Name June 1995 to February 1999 Chief, Accounts Payable Branch

City ,

State

I was responsible for establishing priorities, schedules, and work assignments ensuring changes in workload are accounted for to mmimize
the impact on normal office operations.

This was important during the DFAS Denver directed workload realighment to the Field Sites servicing our customers by Major Command.
Workload increased which dictated frequent priority changes and personnel moves.

I also worked closely with the Major Commands supported by DFAS Limestone strengthening our partnership when workload spikes
negatively impacted our customers.

I was responsible for providing personnel feedback sessions quarterly and preparedsupervisory appraisals of employees’ performance and
potential for advancement.

As a supervisory accountant I was responsible for performmg ongoing analysis of the Vendor Pay workflow and production.

I identified negative trends and weaknesses, ensured specific weaknesses were corrected, and determine whether systemic or repeat issues
were identified and adequately addressed.

I was required to apply a comprehensive knowledge of analysis/reportmg requirements, work processes, vendor pay system structures, and
data produced to resolve these issues.

Utiizmg my knowledge with Louis II data retrieval software, I produced ad-hoc data queries for in-house and external use by our
customers.

These retrievals are all designed to reduce the man- hours necessary to perform complex finance and accounting functions by DFAS and
Arr Force personnel.

I was responsible for the budget resources necessary to operate the branch.

In this capacity, I prepared budget over execution justifications, plan and monitor overtime costs, and control supply purchases to ensure the
most cost efficient operation possible.

I was required to respond to inquiries from various sources, which include, but are not limited to, vendors, DFAS management, accounting
liaison offices, resource advisors, and other DFAS field sites.

These inquiries require my ability to relay technical aspects of systems deficiencies to customers who are not familiar with our operation.

I participated in video teleconferences, conference calls, and briefings designed to address customer and DFAS management requirements.
I was often called upon to explain, in laymen's terms, DFAS policy and procedures with regards to delays in payment due to various
reasons,

I was required to respond to various audit reports and studies; ensuring senior management and audit personnel, understand particular
situations within the Vendor Pay business process that result in these findings.

I was hand selected by the Field Site Director and Vendor Pay Site Manager to represent DFAS Limestone on a team comprised of
representatives from all DFAS Denver field sites to provide traming to our Air Force base level Resource Advisors.

During a five week period, I provided "Boot Camp" trammg to over 400 base level personnel ensuring resource advisors were familiar with
the DFAS structure and mission requirements related to funds management.

Company Name June 1994 to June 1995 Accountant, Network Assistant Team

City ,

State

As a member of the Network Assistance Team, I was required to have an extensive working knowledge of DoD accounting systems,
theory, policy, and procedures.

I was consistently called upon to develop and implement procedures consistent with DoD regulations.

Coordinated with DFAS Denver and the Onmha Field Site on the consolidation of the first geographically separated Defense Accounting
Office into DFAS.

In ny position as a member of the Network Assistance Team | was required, upon arrival at each base level Defense Accounting Office
(DAO) to provide an i~-brief?

This briefing identified team members, the purpose of the visit, goals, and responsibilities.

Upon completion of the assignment, provided a written and oral out-brief outlmg the team accomplishments during the visit.

I provided recommendations to preclude recurring problems and to prepare the organization for consolidation,

Company Name June 1993 to June 1994 Supervisor, Accounts Control Branch

City ,

State

T directed /ameruiced the accamnlichment of all financial renarte and ctatemente

IAI CHUU SUpULIDUAL WY GUO ULUYIDULUGLIL U1 GL LUGE LUPUS GER OUAWELLRLILO.

I was responsible for the completeness and accuracy of weekly, monthly, quarterly, semi-annual, and annual reports.

Monitored errors m the General Accounting and Finance System (GAFS/BQ) and ensured corrective actions were accomplished.

I also ensured fimd balances were reconciled to the appropriate audit listings and verified reports prior to release to base activities and

higher headquarters.

e | furnished accounting data to base organizations offen interpreting and analyzing the data to help finds managers resolve problems and
manage their programs more effectively.

e J attended Major Command (MAJCOM) and Headquarters level workshops to participate and contribute to accounting policy and system
changes.

e | provided professional assistance to Data Automation relevant to processing of accounting and finance data, interpreting deficiencies in
software based on output products and system related problems.

e | utilized my working knowledge of commercial and government accounting system principles and knowledge of Processing Centers (PCs)
to review, verify, analyze, and evaluate accounting and finance operations.

e While serving as Chief} Account Control I ensured areas of concern were addressed, concentrating on problem areas related to the
database.

e | analyzed computer output products to determine processing deficiencies.

e They included, but were not limited to, the Open Document Listing (ODL), Operating Budget Ledger (OBL), Allotment Ledger (AL), and
the Accounting and Finance Workload Information Management System (A&F WIMS) Extract list.

© | provided technical assistance related to policy and procedural.

e changes required as a result of the impending base closure.

e Analyzed/developed and recommended improved training procedures enabling better use of system procedures ensuring governing
directives were followed.

¢ | evaluated accuracy of accounting records prior to fiscal year closeout ensuring the Accounting and Finance Officer could certify their
accuracy as required by regulation.

e Examined accounting transactions and documents to ensure they conformed to established accounting policy and principles.

© Coordinated and directed fiscal year end conversion for the GAFS and Integrated Accounts Payable System (IAPS).

ee @ 1

Education
Northern Maine Community College 1994 Associate : Accounting City , State , USA

Emphasis in Business
1994 Associates : Accounting City , State, USA GPA: GPA: 3.41

Accounting GPA: 3.41 174 Hours, Quarter

Attended Husson College, major Accounting 78 semester hours toward Bachelors degree.

Professional Military Comptroller School, 6wk, 4-98; Managerial Accounting I, 09-98; Interested-Based Bargaining Trammg for Management,
24hrs, 09-01; Auditing Methods and Concepts 09-98; Organizational Leadership, 32hrs, 07-03; Management Development II, 32hrs, 07-03.
Certifications

Certified Defense Financial Manager, CDFM, May 2005

Interests

American Society Of Military Comptrollers

Additional Information

Skills

Accounting; General Accounting; Accounts Payable; Program Management."""


enhance_prompt = """ You are working to enhance the resume of my customers. You will be fed in a resume. Your task is to identify the experience portion of the resume. This would likely 
entail:

Academic Projects
Corporate Experience
Course Projects
Global Experience
Independent Research
Industry Experience
Internship Experience
Military Background
Professional Experience
Related Experience
Related Projects
Work Experience

and whatever else that falls under the umbrella term of "Experience" in a resume.

Output your answer in a valid json file where each role/experience has 4 + n properties + number of bullet point description properties: role, company, duration, 
location, experience bullet point description 1, experience bullet point description 2, ..., experience bullet point description n (for n bullet points). You need to organize such that 
each property is assigned its value from the resume text attached towards the end of this message.  

For the role and company, find what looks like their role and company. 
If the resume includes: Digital Marketing Analyst Intern, Marketing Science Associates the role would be the digital marketing analyst intern 
and the company would be marketing science associates. 

The duration should be the time frame they have listed on their resume. It might look like Jan 2025 - present, January 2025 to present, Feb 2024 - June 2024, etc. Identify the dates. 

The location is pretty self-explanatory. Try to see if they listed a location on the description, if not leave this section blank. 

When creating these experience bullet point descriptions. I want you to take in the original description, then improve it using action verbs, and trying to implement quantitative information.
A format that is sometimes good to follow is Achieved [X] as measured by [Y] by doing [Z] and its variations. You do not have to always use this format, I am just giving it to you as a
guide. 

I want the bullet points to be concise, well articulated, and quantitative. HOWEVER, DO NOT CREATE NUMBERS IF THEY WEREN'T INCLUDED IN THE ORIGINAL. only enhance the material from the input
and do not create fake information that does not agree with the material from the input. If they are missing a metric that would significantly  improve the description, create the a bracket with
a message indicating what the user should do when they are manually editing this output. For example "oversaw the growth of something by [input metric here] to [input metric here] through..." or
"improved model accuracy by [input metric here] by identifying ... " TRY TO USE ALL OF THE METRICS THAT THE USER ALREADY HAS IMPLEMENTED. 

The output should objectively be better than the original information on the input resume. 

Now please create the enhanced resume section for the following resume input: 
"""


cpd_tech_ocr_result = """Name

PO Box 100000, Atlanta GA 30322 303-111-2222 name@emory.edu http://website.com
EDUCATION
Emory University, Emory College, Atlanta, GA May 2022

Bachelor of Science in Mathematics and Computer Science
Cumulative GPA: 3.89/4.00

RELEVANT TECHNICAL SKILLS

Computing Languages and Technologies — Java, C, JUnit, Spring, Windows, Unix
Database Technologies - SQL, PL/SQL, Oracle, MySQL
Web Development — XHTML, CSS, JavaScript, AJAX, Dojo, jQuery, PHP, APEX, XML, XSL

HONORS

2020 Deborah Jackson Award Recipient
Dean’s Achievement Scholar
International Baccalaureate Diploma Recipient

WORK EXPERIENCE

Southwest Airlines, Dallas, TX May 2021 — Aug 2021
Southwest.com Air Team Intern

« Developed new back-end architecture and defect fixes for southwest.com on-line interface

- Engaged in test-driven development practices while demonstrating agile values as part of a team environment

Home Depot Corporate Headquarters, Atlanta, GA May 2019 — Aug 2019, May 2020 — May 2020

Information Technology Intern

- Led several Oracle APEX applications through the development life-cycle, communicating with the business
analysts, creating the data model, and designing the applications

- Designed and implemented new methods for unit tests with the Spring framework

« Optimized and upgraded Java back-end and JavaScript/AJAX front-end of web applications

« Drafted UML technical designs for existing and future projects

Emory University Technology Services, Atlanta, GA Aug 2019 — Aug 2020, Aug 2021 — Present
Clean Room Technician
« Remove malware from computer, resolve software issues and assist with wireless network configuration

Global Health, Education, and Economic Development, Atlanta, GA Jan 2019 — Present
Technical Lead

- Develop a website providing online applications for trips to Guatemala and Nepal

« Implemented collaboration tools for communication among interns and executive board

LEADERSHIP AND COMMUNITY ENGAGEMENT

Volunteer Emory, Atlanta, GA Aug 2018 — Present

Student Co-Director

. Established, recruit participants, and lead a new weekly service trip to Computers for Youth, a program
designed to refurbish computers for low income families

- Coordinating and leading a 2010 spring break trip to Leland, MS to work with Habitat for Humanity

- Support organization with major events throughout the year, including co-leading Gandhi/Be the Change Day

-  Volunteered on service trips to New Orleans, LA and Leland, MS to re-construct homes in 2009/2010

- Volunteered with various agencies, including the Open Door community, Briar Vista Elementary School, and
Jones Boys and Girls Club

PAWS Atlanta, Atlanta, GA Feb 2018 — Aug 2019

Volunteer

« Cleaned kennels, walked and fed the animals, and set up live video feeds

« Worked with assistant manager to repair older kennels for the shelter and helped cut down dead trees for the
shelter to ensure the safety of the animals and neighboring properties

. Raised $200 for PAWS selling t-shirts at the Pets EXPO in Atlanta

ADDITONAL SKILLS AND INTERESTS

Languages: Fluent in Spanish; Conversational in German

Fine Arts: Piano (14 years — high mastery); Sketch and Charcoal Painting (8 years)
Interests: Soccer; Mountain Climbing; Organic Gardening; Strategic Gaming"""

background_categorize_prompt = """ You are a resume section categorizer. Your job is to extract the **background** information from resumes and return it in clean JSON format. The 
background category includes the following information, if available:

- `name`: Full name of the candidate
- `email`: Email address
- `phone_number`: Phone number
- `location`: City and state or general location
- `other_contact`: Any other contact information (LinkedIn, GitHub, etc.) 
There might be additional other contacts, so include as many other_contact_i as possible where i would be the number. 

Return only a JSON object with the background info extracted. I want the output to be in a format like, but if not all sections are indicated, don't add new information. 

{
    "Background": 
    {
        "Name": "XYZ",
        "Email": "XYZ",
        "Phone Number": "XYZ",
        "Location": "XYZ",
        "LinkedIn": "XYZ",
        // Additional contacts as separate key-value pairs if available
    }
}

Make sure that this output makes sense. If you see repeats, only include if necessary. Your goal is to categorize. 


Now categorize the background information:
"""

education_categorize_prompt = """ You are a resume section categorizer. Your task is to extract the **education** section from a resume and return it in clean JSON format. The education section 

includes the following information for each degree or institution listed:

- `degree`: Name of the degree (e.g., B.S. in Marketing)
- `major`: Major or field of study (if separate from degree)
- `school`: Name of the institution
- `location`: City and state or general location
- `date`: Time period of study (start and end dates, if listed)
- `gpa`: GPA, if listed

You may assume there can be multiple entries for education. Only extract what is provided and omit any missing fields.

Return only a JSON object with the education info extracted. Do not include any text outside the JSON object.

for example: 
    {
        "Education": 
        {
            "School 1":
                {
                    "Name": XYZ,
                    "Degree": XYZ,
                    "Time/Graduation year": 123,
                    "Location": 123,
                    ... (anything else that should be included in the background section): (corresponding value)
                },
            "School 2 (if applicable
        }
        
        }
    }

    
Make sure that this output makes sense. If you see repeats, only include if the degree is different. Your goal is to categorize. 
    
Now categorize the education information:


"""

skill_categorize_prompt = """You are a resume section categorizer. Your job is to extract or infer the **skills and interests** from a resume and return them in clean JSON format. Use only the information exclusively from the input resume.

Guidelines:
- If the resume includes an explicit skills section, extract the listed skills.
- If there is no dedicated skills section, analyze the resume content (including job experience, project descriptions, tools, etc.) and infer the skills the candidate likely possesses.
- Group the skills under categories if applicable. Otherwise, return a flat list.
- The final output must be a valid JSON object with a single top-level key "Skills" (or "Skills and Interests") and the following keys inside if data is available:
  - `skills`: A string containing a comma-separated list of primary technical skills (keep it concise and at most 7 words overall).
  - `languages`: A string with language proficiencies (if available).
  - `interests`: A string with interests (if available).
- Each key should be at the same level (flat structure). Do not nest these fields inside any additional objects.
- Do not include any text outside the JSON object.
- Ensure that the final output strictly adheres to the format shown below. If a particular field is missing in the resume, omit that key or leave it empty as appropriate.

Example output format:
{
    "Skills": {
        "skills": "Java, C, SQL",
        "languages": "Spanish (Fluent), German (Conversational)",
        "interests": "Soccer, Mountain Climbing"
    }
}

Now categorize the skills:
"""

experience_categorize_prompt = """ You are a resume section categorizer. You will be fed in a resume. Your task is to identify the experience portion of the resume. This would likely 
entail:

Academic Projects
Corporate Experience
Course Projects
Global Experience
Independent Research
Industry Experience
Internship Experience
Military Background
Professional Experience
Related Experience
Related Projects
Work Experience

and whatever else that falls under the umbrella term of "Experience" in a resume.

Output your answer in a valid json file where each role/experience has 4 + n properties + number of bullet point description properties: role, company, duration, 
location, experience bullet point description 1, experience bullet point description 2, ..., experience bullet point description n (for n bullet points). You need to organize such that 
each property is assigned its value from the resume text attached towards the end of this message.  
 
I want this to be in this format: 
    {
        "Experience": 
        {
            "Experience 1":
                {
                    "role": XYZ,
                    "company": XYZ,
                    "duration": 123,
                    "location": 123,
                    "bullet_point1": XYZ,
                    "bullet_point2": XYZ,
                    ... 
                },
            "Experience2 (if applicable":
                {
                ...
                }
        }
        
        }
    }

PLEASE USE YOUR INTUITION, IF IT DOES NOT LOOK LIKE IT WOULD FALL IN THE EXPERIENCE SECTION OF A RESUME, DON'T INCLUDE IT. 
DO NOT MAKE UNNECESSARY REPEATS AND MAKE SURE YOUR NET GOAL IS CATEGORIZATION

    
Use exclusively the information from the resume. Now categorize the following: 
"""



misc_categorize_prompt = """ You are a resume section categorizer. Your task is to extract any resume content that does **not** fall under the following categories: background, education, skills, or experience.

Here is how the previous categories mentioned might be categorized: 
{
    "Background": 
    {
        "Name": "XYZ",
        "Email": "XYZ",
        "Phone Number": "XYZ",
        "Location": "XYZ",
        "LinkedIn": "XYZ",
        "Current Role": "XYZ"
        // Additional contacts as separate key-value pairs if available
    }
}


{
        "Experience": 
        {
            "Experience 1":
                {
                    "role": XYZ,
                    "company": XYZ,
                    "duration": 123,
                    "location": 123,
                    "bullet_point1": XYZ,
                    "bullet_point2": XYZ,
                    ... 
                },
            "Experience2 (if applicable":
                {
                ...
                }
        }
        
        }
    }

Your goal is to group the remaining content into meaningful subsections, label them appropriately, and return the result in a clean JSON structure. The top-level keys of the JSON file should be the names of each detected subsection (e.g., `"Leadership"`, `"Projects"`).

DO NOT INCLUDE A SKILLS AND INTEREST SECTION. USE YOUR COMMON SENSE TO INCLUDE EVERYTHING THAT MIGHT NOT FALL UNDER EXPERIENCE,BACKGROUND,SKILLS/INTERESTS, AND EDUCATION.
this means that you do not include their technical skills or languages or interests that might be written in the original resume. SO IF YOU SEE WORDS LIKE INTEREST OR SKILLS, MAKE 
SURE YOU EXCLUDE THEM FROM YOUR RESPONSE.

IE DO NOT INCLUDE ANYTHING LIKE: 
"Additional Skills and Interests": {
        "Languages": {
            "Fluent in Spanish": true,
            "Conversational in German": true
        },
        "Fine Arts": {
            "Piano (14 years — high mastery)": true,
            "Sketch and Charcoal Painting (8 years)": true
        },
        "Interests": ["Soccer", "Mountain Climbing", "Organic Gardening", "Strategic Gaming"]
    }

Return only a JSON object with the miscellaneous information extracted and properly grouped. Do not include any text outside the JSON object.

USE YOUR COMMON SENSE TO MAKE SURE THAT THE INFORMATION IS NOT REPETITIVE AND THE RIGHT MATERIAL IS INCLUDED IN THIS SECTION

Now categorize the miscellaneous content from the following:

"""


def experience_enhancer(prompt, ocr_result):
    response = client.responses.create(
        model = "gpt-3.5-turbo",
        input = prompt + "" + ocr_result
    )
    return response.output_text

def categorize_prompt(prompt, ocr_result):
    response = client.responses.create(
        model = "gpt-3.5-turbo",
        input = prompt + "" + ocr_result

    )
    return response.output_text

def categorize_combiner(ocr_result):
    background = categorize_prompt(background_categorize_prompt,ocr_result)
    education = categorize_prompt(education_categorize_prompt,ocr_result)
    experience = categorize_prompt(experience_categorize_prompt,ocr_result)
    skills = categorize_prompt(skill_categorize_prompt,ocr_result)
    misc = categorize_prompt(misc_categorize_prompt,ocr_result)
    net_resume = [background, education, experience, skills, misc]
    parsed_resume = {}
    for idx, section in enumerate(net_resume):
        section_str = section.strip()
        section_str = clean_json_string(section_str)
        if not section_str:
            print(f"Warning: Section{idx} returned an empty response.")
            continue
        try:
            section_dict = json.loads(section_str)

            parsed_resume.update(section_dict)

        except json.decoder.JSONDecodeError as e:
            print(f"JSON decode error in section {idx}:", section_str)

    final_json = json.dumps(parsed_resume, indent=4)
    return final_json

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

def suggestion_experience(ocr_result):
    # TODO: implement the method to give proper tips on the 
    return None



def repeat_checker(combined):

    return None

"""
{
    "Background": {
        "Name": "Not provided",
        "Email": "Not provided",
        "Phone Number": "303-111-2222",
        "Location": "Atlanta, GA",
        "Other Contact 1": "http://website.com"
    },
    "Education": {
        "Degree 1": {
            "School": "Emory University, Emory College",
            "Degree": "Bachelor of Science in Mathematics and Computer Science",
            "Location": "Atlanta, GA",
            "Date": "May 2022",
            "GPA": "3.89/4.00"
        }
    },
    "Experience": {
        "Experience 1": {
            "role": "Southwest.com Air Team Intern",
            "company": "Southwest Airlines",
            "duration": "May 2021 \u2014 Aug 2021",
            "location": "Dallas, TX",
            "bullet_point1": "Developed new back-end architecture and defect fixes for southwest.com on-line interface",
            "bullet_point2": "Engaged in test-driven development practices while demonstrating agile values as part of a team environment"
        },
        "Experience 2": {
            "role": "Information Technology Intern",
            "company": "Home Depot Corporate Headquarters",
            "duration": "May 2019 \u2014 Aug 2019, May 2020 \u2014 May 2020",
            "location": "Atlanta, GA",
            "bullet_point1": "Led several Oracle APEX applications through the development life-cycle, communicating with the business analysts, creating the data model, and designing the applications",
            "bullet_point2": "Designed and implemented new methods for unit tests with the Spring framework"
        },
        "Experience 3": {
            "role": "Clean Room Technician",
            "company": "Emory University Technology Services",
            "duration": "Aug 2019 \u2014 Aug 2020, Aug 2021 \u2014 Present",
            "location": "Atlanta, GA",
            "bullet_point1": "Remove malware from computer, resolve software issues and assist with wireless network configuration"
        },
        "Experience 4": {
            "role": "Technical Lead",
            "company": "Global Health, Education, and Economic Development",
            "duration": "Jan 2019 \u2014 Present",
            "location": "Atlanta, GA",
            "bullet_point1": "Develop a website providing online applications for trips to Guatemala and Nepal",
            "bullet_point2": "Implemented collaboration tools for communication among interns and executive board"
        }
    },
    "Skills": {
        "skills": "Java, C, SQL, JavaScript, AJAX, Spring, Oracle",
        "languages": "Spanish (Fluent), German (Conversational)",
        "interests": "Soccer, Mountain Climbing, Organic Gardening, Strategic Gaming"
    },
    "Leadership and Community Engagement": {
        "Volunteer Emory, Atlanta, GA Aug 2018 \u2014 Present": {
            "Position": "Student Co-Director",
            "Responsibilities": [
                "Established, recruited participants, and led a new weekly service trip to Computers for Youth, a program designed to refurbish computers for low-income families",
                "Coordinated and led a 2010 spring break trip to Leland, MS to work with Habitat for Humanity",
                "Supported organization with major events throughout the year, including co-leading Gandhi/Be the Change Day",
                "Volunteered on service trips to New Orleans, LA and Leland, MS to reconstruct homes in 2009/2010",
                "Volunteered with various agencies, including the Open Door community, Briar Vista Elementary School, and Jones Boys and Girls Club"
            ]
        },
        "PAWS Atlanta, Atlanta, GA Feb 2018 \u2014 Aug 2019": {
            "Position": "Volunteer",
            "Responsibilities": [
                "Cleaned kennels, walked and fed the animals, and set up live video feeds",
                "Worked with assistant manager to repair older kennels for the shelter and helped cut down dead trees for the shelter to ensure the safety of the animals and neighboring properties",
                "Raised $200 for PAWS selling t-shirts at the Pets EXPO in Atlanta"
            ]
        }
    }
}
"""

if __name__ == "__main__":
    print(categorize_combiner(cpd_tech_ocr_result))
    #print(experience_enhanced)
    #with open("experience.json", "w") as json_file:
        #json.dump(experience_enhanced, json_file, indent=4)

