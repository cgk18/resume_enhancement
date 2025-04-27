import pandas as pd 
import numpy as np
import pytesseract
from pdf2image import convert_from_path
import re
import cv2
from PIL import Image

from numpy import linalg
from math import sqrt
from math import atan
from math import pow
import glob
import os




# resume_df = pd.read_csv("dat/Resume/Resume.csv")
# print(resume_df.head) # check the resume format

# print(resume_df.iloc[0]['Resume_str']) # check material in the resume. 

'''test before creating funciton'''
# image = cv2.imread("resume_enhancement/dat/data/data/ACCOUNTANT/10554236.pdf")
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # doesn't run unfortunately. 
# text = pytesseract.image_to_string(gray_image) 


'''
OCR attempt on the resume data. 
'''

# pdf_path = "resume_enhancement/dat/data/data/ACCOUNTANT/10554236.pdf"

def ocr(path,dpi = 300):
    pages = convert_from_path(path,dpi = dpi)
    extracted_text = ""

    for i, page in enumerate(pages):
        open_cv_image = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        # threshold using savuola's binarization instead:
        # thresh = sauvola_binarize(open_cv_image)
        text = pytesseract.image_to_string(thresh)
        extracted_text += text + "\n"

    return extracted_text

'''
put the material extracted from the ocr into different categories. 
'''
def extract_resume_text(text):
    resume_data = {}
    education_match = re.search(r"Education(.*?)(Experience|Skills|Certifications|$)", text, re.DOTALL | re.IGNORECASE)
    if education_match:
        resume_data["education"] = education_match.group(1).strip()

    experience_match = re.search(r"Experience(.*?)(Education|Skills|Certifications|$)", text, re.DOTALL | re.IGNORECASE)
    if experience_match:
        resume_data["experience"] = experience_match.group(1).strip()


    skills_match = re.search(r"Skills(.*?)(Experience|Education|Certifications|$)", text, re.DOTALL | re.IGNORECASE)
    if skills_match:
        resume_data["skills"] = skills_match.group(1).strip()

    summary_match = re.search(r"Summary(.*?)(Highlights|Experience|$)", text, re.DOTALL | re.IGNORECASE)
    if summary_match:
        resume_data["summary"] = summary_match.group(1).strip()
    
    certifications_match = re.search(r"Certifications(.*?)(Skills|Experience|Education|$)", text, re.DOTALL | re.IGNORECASE)
    if certifications_match:
        resume_data["certifications"] = certifications_match.group(1).strip()
    
    return resume_data

'''
Work with headers instead of just looking for the specific word 
'''



def sauvola_binarize(gray_img, window=15, k=0.2, r=128):
    img = gray_img.astype(np.float64)

    h, w = img.shape
    b = cv2.integral(img)      
    c = cv2.integral(img**2)   

    bin_img = np.zeros_like(img, dtype=np.uint8)
    half_win = window // 2

    for y in range(h):
        for x in range(w):
            
            y1 = max(0, y - half_win)
            y2 = min(h - 1, y + half_win)
            x1 = max(0, x - half_win)
            x2 = min(w - 1, x + half_win)

            region_height = (y2 - y1 + 1)
            region_width  = (x2 - x1 + 1)
            region_size   = region_height * region_width

            sum_region = b[y2+1, x2+1] - b[y2+1, x1] - b[y1, x2+1] + b[y1, x1]
            sum_sq_region = c[y2+1, x2+1] - c[y2+1, x1] - c[y1, x2+1] + c[y1, x1]

            m = sum_region / region_size

            var = (sum_sq_region / region_size) - (m * m)

            std_dev = math.sqrt(var) if var > 0 else 0


            T = m * (1 + k * ((std_dev / r) - 1))


            if img[y, x] < T:
                bin_img[y, x] = 0
            else:
                bin_img[y, x] = 255

    bin_img[:half_win, :] = 255
    bin_img[:, :half_win] = 255
    bin_img[h-half_win:, :] = 255
    bin_img[:, w-half_win:] = 255

    # Calculate how much of the image is white and invert if necessary:
    white_ratio = np.sum(bin_img == 255) / bin_img.size

    if white_ratio <.5:
        bin_img = cv2.bitwise_not(bin_img)

    return bin_img


def extract_header_first(text):
    headers = ["Education", "Experience", "Skills", "Certifications", "Summary"]
    resume_data = {}
    current_header = None

    lines = text.splitlines()


    for line in lines:
        stripped_line = line.strip()
        header_found = False
        for header in headers:
        
            if re.fullmatch(rf"{header}[:]?(\s*)", stripped_line, flags=re.IGNORECASE):
                current_header = header.lower()  
                resume_data[current_header] = ""  
                header_found = True
                break

        if not header_found and current_header:
            resume_data[current_header] += stripped_line + "\n"

    for key in resume_data:
        resume_data[key] = resume_data[key].strip()

    return resume_data





if __name__ == "__main__":
    test_path = "dat/alternative_styles/tech_emory_cpd.pdf"
    test_text = ocr(test_path)
    print(test_text)

    """sasha_test_path = "dat/alternative_styles/sasha_wagner.pdf"
    sasha_text = ocr(sasha_test_path)
    print("\nsasha text:")
    print(sasha_text)"""
    #extract_test = extract_resume_text(test_text)
    # extract_header = extract_header_first(test_text)
    #print(extract_header)
