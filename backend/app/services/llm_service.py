from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from app.config import OPENAI_API_KEY

llm = ChatOpenAI(
    temperature=0,
    openai_api_key=OPENAI_API_KEY,
    model="gpt-4o-mini"
)

summary_prompt = PromptTemplate(
    input_variables=["resume", "job_description"],
    template="""
You are an AI recruiter.

Analyze the resume against the job description.

Resume:
{resume}

Job Description:
{job_description}

Provide:
1. Match Score (0-100)
2. Strengths
3. Missing Skills
4. Final Recommendation
"""
)

def generate_summary(resume, job_description):
    chain = summary_prompt | llm

    response = chain.invoke({
        "resume": resume,
        "job_description": job_description
    })

    return response.content
