from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Create Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Prompt Template
template = PromptTemplate(
    input_variables=["topic"],
    template="""
Explain {topic} using exactly this format.

Name:
Definition:
Advantages:
Example:
"""
)

# User Input
topic = input("Enter topic: ")

# Fill template
prompt = template.format(topic=topic)

# AI Response
response = llm.invoke(prompt)

print("\n========== AI OUTPUT ==========\n")

print(response.content)