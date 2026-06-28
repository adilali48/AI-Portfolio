from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

topic = input("Enter a topic: ")

# Step 1: Explain
explanation = llm.invoke(
    f"Explain {topic} in simple English."
).content

# Step 2: Summarize
summary = llm.invoke(
    f"Summarize this in 3 bullet points:\n\n{explanation}"
).content

# Step 3: Translate
urdu = llm.invoke(
    f"Translate this into simple Urdu:\n\n{summary}"
).content

print("\n========== EXPLANATION ==========\n")
print(explanation)

print("\n========== SUMMARY ==========\n")
print(summary)

print("\n========== URDU ==========\n")
print(urdu)