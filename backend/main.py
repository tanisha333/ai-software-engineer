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

        question = input("\nYou: ")

        if question.lower() == "exit":
            break

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

        if isinstance(response.content, list):
            for item in response.content:
                if item.get("type") == "text":
                    print(item["text"])
        else:
            print(response.content)


if __name__ == "__main__":
    main()