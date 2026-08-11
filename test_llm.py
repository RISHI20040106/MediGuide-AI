from rag.llm import get_llm


def main():

    llm = get_llm()

    question = "What is hypertension?"

    response = llm.invoke(question)

    print("\nQuestion:")
    print(question)

    print("\nResponse:")
    print("-" * 80)
    print(response.content)


if __name__ == "__main__":
    main()