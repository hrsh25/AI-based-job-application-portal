from .models import Job
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
import pandas as pd
import spacy
from spacy.matcher import Matcher
import re

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as fh:
        # iterate over all pages of PDF document
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            # creating a resource manager
            resource_manager = PDFResourceManager()

            # create a file handle
            fake_file_handle = io.StringIO()

            # creating a text converter object
            converter = TextConverter(
                resource_manager,
                fake_file_handle,
                codec='utf-8',
                laparams=LAParams()
            )

            # creating a page interpreter
            page_interpreter = PDFPageInterpreter(
                resource_manager,
                converter
            )

            # process current page
            page_interpreter.process_page(page)

            # extract text
            text = fake_file_handle.getvalue()
            yield text

            # close open handles
            converter.close()
            fake_file_handle.close()

# calling above function and extracting text
text = ''

for page in extract_text_from_pdf('C:\\Users\\harsh\\Downloads\\CV.pdf'):
    text += ' ' + page

nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)

def extract_name(resume_text):
    nlp_text = nlp(resume_text)

    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]

    matcher.add('NAME', None, [{'POS': 'PROPN'}, {'POS': 'PROPN'}])
    matches = matcher(nlp_text)

    for match_id, start, end in matches:
        span = nlp_text[start:end]
        return span.text


def extract_mobile_number(text):
    phone = re.findall(re.compile(
        r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'),text)

    if phone:
        number = ''.join(phone[0])
        if len(number) > 10:
            return '+' + number
        else:
            return number

def extract_email(email):
    email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", email)
    if email:
        try:
            return email[0].split()[0].strip(';')
        except IndexError:
            return None

def get_skills():
    return Job.objects.all()


def extract_skills(resume_text):
    nlp_text = nlp(resume_text)
    noun_chunks = nlp_text.noun_chunks

    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    # reading the csv file
    data = pd.read_csv("jobs/static/jobs/skills.csv")

    all_skills = list(data.columns.values)

    global skillset
    skillset=[]
    # check for one-grams (example: python)
    for token in tokens:
        if token.lower() in all_skills:
            skillset.append(token.lower())

    # check for bi-grams and tri-grams (example: machine learning)
    for token in noun_chunks:
        token = token.text.lower().strip()
        if token in all_skills:
            skillset.append(token.lower())

    return [i.capitalize() for i in set([i.lower() for i in skillset])]

def get_matching_skills():

    values = get_skills()
    matching_skills=[]
    for temp in values:
        required_skills = temp.Skills.lower().split(',')
        for x in required_skills:
            if x in skillset:
                matching_skills = temp.Skills
            print("Matching Skills: " + matching_skills)
            return matching_skills

#print(extract_skills(text))