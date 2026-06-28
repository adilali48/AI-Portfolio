from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Load .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
)

# Create Prompt Template
template = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple words with an example."
)

# Take input
topic = input("Enter topic: ")

# Create final prompt
prompt = template.format(topic=topic)

# Ask AI
response = llm.invoke(prompt)

print("\n========== AI Answer ==========\n")
print(response.content)