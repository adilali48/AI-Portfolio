from agent import llm
from tools import calculator, current_date, current_time

print("=" * 60)
print("🤖 AI Agent")
print("=" * 60)

while True:

    question = input("\nAsk: ")

    if question.lower() == "exit":
        break

    lower = question.lower()

    if "date" in lower:
        print(current_date.invoke({}))
        continue

    if "time" in lower:
        print(current_time.invoke({}))
        continue

    if lower.startswith("calc"):

        expression = question.replace("calc", "").replace(":", "").strip()

        print(calculator.invoke({"expression": expression}))
        continue

    response = llm.invoke(question)

    print("\n🤖")
    print(response.content)