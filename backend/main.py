from langchain_core.messages import HumanMessage

from graphs.graph_builder import build_graph

app = build_graph()

config = {
    "configurable": {
        "thread_id": "software-engineer"
    }
}


def main():

    print("=" * 60)
    print("🤖 AI Software Engineer")
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:

        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("\n👋 Goodbye!")
            break

        try:

            result = app.invoke(
                {
                    "messages": [
                        HumanMessage(content=question)
                    ]
                },
                config=config
            )

            print("\nAI:\n")

            response = result["messages"][-1]
            content = response.content

            if isinstance(content, str):
                print(content)

            elif isinstance(content, list):

                for item in content:

                    if isinstance(item, dict):
                        if item.get("type") == "text":
                            print(item.get("text", ""), end="")

                    elif isinstance(item, str):
                        print(item, end="")

                    else:
                        print(str(item), end="")

                print()

            else:
                print(content)

        except Exception as e:
            error = str(e)
            print()
            if "429" in error or "RESOURCE_EXHAUSTED" in error:
                print("❌ Gemini API quota exceeded.")
                print("Please try again later or use another API key.")
            elif "404" in error:
                print("❌ Resource not found.")
            else:
                print(f"❌ Error: {error}")

if __name__ == "__main__":
    main()