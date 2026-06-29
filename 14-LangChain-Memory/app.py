from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

chat_history = []

print("AI Chatbot (type 'exit' to quit)\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    chat_history.append(f"User: {question}")

    prompt = f"""
You are a helpful AI assistant.

Conversation History:
{chr(10).join(chat_history)}

Reply to the user's latest message.
"""

    response = llm.invoke(prompt)

    answer = response.content

    print("\nAI:", answer, "\n")

    chat_history.append(f"AI: {answer}")