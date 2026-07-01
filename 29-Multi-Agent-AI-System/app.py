from graph import graph

print("=" * 60)
print("🤖 Multi-Agent AI System")
print("=" * 60)

while True:

    query = input("\nAsk Anything (type exit to quit): ")

    if query.lower() == "exit":
        break

    result = graph.invoke({
        "query": query
    })

    print("\n" + "=" * 60)

    print("\n🔍 Research Agent Output\n")
    print(result["research"])

    print("\n" + "-" * 60)

    print("\n💻 Coding Agent Output\n")
    print(result["code"])

    print("\n" + "=" * 60)