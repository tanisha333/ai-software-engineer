from langchain_core.messages import HumanMessage

from graph.builder import build_graph

app = build_graph()

config = {
    "configurable": {
        "thread_id": "software-engineer-session"
    }
}


def main():

    print("🤖 AI Software Engineer")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You: ")

        if question.lower() == "exit":
            print("Goodbye!")
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

        print(result["messages"][-1].content)

        print()


if __name__ == "__main__":
    main()