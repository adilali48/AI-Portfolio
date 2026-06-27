import os
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("Ab8RN6L48eeuneKUFUW1Ub6PicugHJgpExCpQKTai0n0Luq7Lw")
)

print("🤖 AI Chatbot Started!")
print("Type 'exit' to quit.\n")

chat_history = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("\n===== Chat History =====")
        for message in chat_history:
            print(f"{message['role']}: {message['text']}")
        print("Goodbye!")
        break

    # Save user message
    chat_history.append({"role": "user", "text": user_input})

    # Get AI response
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    # Save AI response
    chat_history.append({"role": "assistant", "text": response.text})

    print("\nAI:", response.text)
    print("-" * 50)