from langchain_core.messages import HumanMessage

from agent.agent import agent


THREAD_ID = "customer-session-1"


def run_agent(question: str) -> str:

    result = agent.invoke(
        {
            "messages": [
                HumanMessage(content=question)
            ]
        }
    )

    last_message = result["messages"][-1]

    content = last_message.content

    if isinstance(content, list):

        response = ""

        for item in content:

            if isinstance(item, dict):

                if item.get("type") == "text":

                    response += item.get("text", "")

        return response.strip()

    return str(content)


def main():

    print("=" * 60)
    print("🛒 AI Customer Support Agent")
    print("=" * 60)
    print("Type 'exit' to quit.")

    while True:

        question = input("\nYou : ").strip()

        if question.lower() == "exit":
            print("\nThank you for using the AI Store Assistant!")
            break

        if not question:
            continue

        try:

            answer = run_agent(question)

            print("\nAgent :", answer)

        except Exception as e:

            print("\nError:", e)


if __name__ == "__main__":
    main()