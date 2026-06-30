from tools import search_web
from report_generator import generate_report

print("=" * 60)
print("📚 AI Research Assistant")
print("=" * 60)

topic = input("\nEnter Research Topic: ")

print("\n🔍 Researching...")

results = search_web(topic)

context = ""

for item in results:

    context += item["content"] + "\n\n"

print("🤖 Generating Report...\n")

report = generate_report(topic, context)

print(report)