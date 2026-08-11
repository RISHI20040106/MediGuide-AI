from rag.prompt import get_prompt


def main():

    prompt = get_prompt()

    formatted_prompt = prompt.format(
        context="High fever, headache, nausea.",
        question="What are the symptoms of dengue?"
    )

    print(formatted_prompt)


if __name__ == "__main__":
    main()