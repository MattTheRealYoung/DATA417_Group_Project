from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader, TextLoader
import os

OPEN_API_KEY= ""
os.environ["OPENAI_API_KEY"] = OPEN_API_KEY

def compare_job_description_and_resume(job_description, resume):
    llm = ChatOpenAI(api_key=OPEN_API_KEY)
    prompt = f"""
        Job description: {job_description}
        
        Resume: {resume}
        
        Compare the job description and resume. give a score of similarity between 0 and 1, List the matching skills, experiences, and qualifications.
        Identify any gaps or areas where the resume does not meet the job description requirements. 
    """
    response = llm.invoke(prompt)
    return response

pdfLoader = PyPDFLoader("resume.pdf")
resume = pdfLoader.load_and_split()
resume = resume.pop().page_content

descLoader = TextLoader("jobtype.txt")
job_description = descLoader.load()
job_description = job_description.pop().page_content

print(f"This is resume : {resume}")
print(f"This is job description : {job_description}")

result = compare_job_description_and_resume(job_description, resume)
print(result.content)


