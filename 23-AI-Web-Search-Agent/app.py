from tools import web_search
from agent import llm

print("=" * 60)
print("🌐 AI Web Search Agent")
print("=" * 60)

while True:

    question = input("\nAsk Anything (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    results = web_search(question)

    context = ""

    for item in results:
        context += item["content"] + "\n\n"

    prompt = f"""
You are a helpful AI assistant.

Use ONLY the information below.

Context:

{context}

Question:

{question}
"""

    response = llm.invoke(prompt)

    print("\n🤖 Answer:\n")
    print(response.content)