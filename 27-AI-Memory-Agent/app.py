from agent import llm

chat_history = []

print("=" * 60)
print("🤖 AI Memory Agent")
print("=" * 60)

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    chat_history.append(f"User: {user}")

    prompt = f"""
You are a helpful AI assistant.

Here is the conversation history:

{chr(10).join(chat_history)}

Reply naturally while remembering previous messages.
"""

    response = llm.invoke(prompt)

    answer = response.content

    print("\nAI:", answer)

    chat_history.append(f"Assistant: {answer}")