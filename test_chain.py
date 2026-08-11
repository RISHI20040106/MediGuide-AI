from rag.chain import ask_question


def main():

    question = "What are the symptoms of dengue?"

    result = ask_question(question)

    print("\nQuestion:")
    print(question)

    print("\nAnswer:")
    print("=" * 80)
    print(result["answer"])

    print("\nSources:")
    print("=" * 80)

    for doc in result["documents"]:
        source = doc.metadata.get("source", "Unknown")
        page = doc.metadata.get("page", "N/A")

        if isinstance(page, int):
            page += 1  # Convert to human-friendly page number

        print(f"{source} (Page {page})")


if __name__ == "__main__":
    main()