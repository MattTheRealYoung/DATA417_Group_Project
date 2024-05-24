#LLM Solution Explaination
Here we use the exist resume and job description files which under the same path. Integrated OpenAI APIs by Langchain. Leverage the API to calculate the similarity between resume and job description, also provide us missing skills and experiences.

### Input
- A pdf resume
- A "jobtype" text document

### Prompt
This promopt is the text we are going to ask in LLM. 
- Compare the job description and resume. give a score of similarity between 0 and 100 percentages, List the matching skills, experiences, and qualifications.Identify any gaps or areas where the resume does not meet the job description requirements.

### Output
The code will output the similarity score percentage, also including the miss parts of both files.