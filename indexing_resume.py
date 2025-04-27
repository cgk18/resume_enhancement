import re
import textstat
import language_tool_python
from nltk.tokenize import word_tokenize, sent_tokenize

'''
Dictionary of the action words: 
'''

action_verbs_leadership = {
    "Accomplished", "Achieved", "Administered", "Analyzed", "Assigned", "Attained", "Chaired", "Consolidated",
    "Contracted", "Coordinated", "Delegated", "Developed", "Directed", "Earned", "Evaluated", "Executed",
    "Handled", "Headed", "Impacted", "Improved", "Increased", "Led", "Mastered", "Orchestrated",
    "Organized", "Oversaw", "Planned", "Predicted", "Prioritized", "Produced", "Proved", "Recommended",
    "Regulated", "Reorganized", "Reviewed", "Scheduled", "Spearheaded", "Strengthened", "Supervised", "Surpassed"
}

action_verbs_communication = {
    "Addressed", "Arbitrated", "Arranged", "Authored", "Collaborated", "Convinced", "Corresponded", "Delivered",
    "Developed", "Directed", "Documented", "Drafted", "Edited", "Energized", "Enlisted", "Formulated",
    "Influenced", "Interpreted", "Lectured", "Liaised", "Mediated", "Moderated", "Negotiated", "Persuaded",
    "Presented", "Promoted", "Publicized", "Reconciled", "Recruited", "Reported", "Rewrote", "Spoke",
    "Suggested", "Synthesized", "Translated", "Verbalized", "Wrote"
}

action_verbs_research = {
    "Clarified", "Collected", "Concluded", "Conducted", "Constructed", "Critiqued", "Derived", "Determined",
    "Diagnosed", "Discovered", "Evaluated", "Examined", "Extracted", "Formed", "Identified", "Inspected",
    "Interpreted", "Interviewed", "Investigated", "Modeled", "Organized", "Resolved", "Reviewed", "Summarized",
    "Surveyed", "Systematized", "Tested"
}

action_verbs_technical = {
    "Assembled", "Built", "Calculated", "Computed", "Designed", "Devised", "Engineered", "Fabricated",
    "Installed", "Maintained", "Operated", "Optimized", "Overhauled", "Programmed", "Remodeled", "Repaired",
    "Solved", "Standardized", "Streamlined", "Upgraded"
}

action_verbs_teaching = {
    "Adapted", "Advised", "Clarified", "Coached", "Communicated", "Coordinated", "Demystified", "Developed",
    "Enabled", "Encouraged", "Evaluated", "Explained", "Facilitated", "Guided", "Informed", "Instructed",
    "Persuaded", "Set Goals", "Stimulated", "Studied", "Taught", "Trained"
}

action_verbs_quantitative = {
    "Administered", "Allocated", "Analyzed", "Appraised", "Audited", "Balanced", "Budgeted", "Calculated",
    "Computed", "Developed", "Forecasted", "Managed", "Marketed", "Maximized", "Minimized", "Planned",
    "Projected", "Researched"
}

action_verbs_creative = {
    "Acted", "Composed", "Conceived", "Conceptualized", "Created", "Customized", "Designed", "Developed",
    "Directed", "Established", "Fashioned", "Founded", "Illustrated", "Initiated", "Instituted", "Integrated",
    "Introduced", "Invented", "Originated", "Performed", "Planned", "Published", "Redesigned", "Revised",
    "Revitalized", "Shaped", "Visualized"
}

action_verbs_helping = {
    "Assessed", "Assisted", "Clarified", "Coached", "Counseled", "Demonstrated", "Diagnosed", "Educated",
    "Enhanced", "Expedited", "Facilitated", "Familiarized", "Guided", "Motivated", "Participated", "Proposed",
    "Provided", "Referred", "Rehabilitated", "Represented", "Served", "Supported"
}

action_verbs_organizational = {
    "Approved", "Accelerated", "Added", "Arranged", "Broadened", "Cataloged", "Centralized", "Changed",
    "Classified", "Collected", "Compiled", "Completed", "Controlled", "Defined", "Dispatched", "Executed",
    "Expanded", "Gained", "Gathered", "Generated", "Implemented", "Inspected", "Launched", "Monitored",
    "Operated", "Organized", "Prepared", "Processed", "Purchased", "Recorded", "Reduced", "Reinforced",
    "Retrieved", "Screened", "Selected", "Simplified", "Sold", "Specified", "Steered", "Structured",
    "Systematized", "Tabulated", "Unified", "Updated", "Utilized", "Validated", "Verified"
}

ACTION_VERBS = {'led', 'developed', 'implemented', 'designed', 'managed', 'executed'} # test set
tool = language_tool_python.LanguageTool('en-US')

def compute_readability(text):
    score = textstat.flesch_reading_ease(text)
    normalized = max(0,min(score,100))/100
    return normalized

def compute_conciseness(text, target_word_count):
    target_word_count = 30
    words = word_tokenize(text)
    word_count = len(words)
    conciseness = 1 - abs(word_count - target_word_count) / target_word_count

# def compute_action_orientation(text):
''' needs to be fixed'''

def compute_action_orientation(text):
    words = word_tokenize(text.lower())
    action_count = sum(1 for word in words if word in ACTION_VERBS)
    sentences = sent_tokenize(text)
    if sentences:
        score = action_count / len(sentences)
    else:
        score = 0
    return score   

def compute_quantifiable_achievements(text):
    numbers = re.findall(r'\d+(?:\.\d+)?', text)
    percentages = re.findall(r'\d+%', text)

    total_quantifiable = len(numbers) + len(percentages)

    sentences = sent_tokenize(text)
    if sentences:
        score = total_quantifiable / len(sentences)
    else:
        score = 0
    return score

INDUSTRY_KEYWORDS = {}
def compute_specificity(text):
    
    score = 0
    for keyword in INDUSTRY_KEYWORDS:
        score += text.lower().count(keyword.lower())
    
    sentences = sent_tokenize(text)
    if sentences:
        return score / len(sentences)
    return score


def compute_grammar(text):
    
    matches = tool.check(text)
    sentences = sent_tokenize(text)
   
    errors_per_sentence = len(matches) / len(sentences) if sentences else len(matches)
    
    score = 1 / (1 + errors_per_sentence)
    return score

def score_description(text):
    # Compute individual metrics
    readability = compute_readability(text)
    conciseness = compute_conciseness(text)
    action = compute_action_orientation(text)
    quantifiable = compute_quantifiable_achievements(text)
    specificity = compute_specificity(text)
    grammar = compute_grammar(text)
    
    # Define weights for each metric (these can be adjusted based on your priorities)
    weights = {
        'readability': 0.2,
        'conciseness': 0.2,
        'action': 0.2,
        'quantifiable': 0.2,
        'specificity': 0,
        'grammar': 0.2
    }
    final_score = (weights['readability'] * readability +
                   weights['conciseness'] * conciseness +
                   weights['action'] * action +
                   weights['quantifiable'] * quantifiable +
                   weights['specificity'] * specificity +
                   weights['grammar'] * grammar)

if __name__ == "__main__":
    sample_text = ("Led a team of developers to design and implement a new software system. "
                   "Increased efficiency by 20% through innovative data analysis and process optimization.")
    score = score_description(sample_text)
    print("Final score:", score)