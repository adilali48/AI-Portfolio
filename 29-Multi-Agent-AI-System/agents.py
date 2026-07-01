import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)


def research_agent(query):
    prompt = f"""
You are a professional research assistant.

Research the following topic carefully:

{query}
"""

    return llm.invoke(prompt).content


def coding_agent(query):
    prompt = f"""
You are an expert Python developer.

Write code or explain programming concepts.

Task:

{query}
"""

    return llm.invoke(prompt).content