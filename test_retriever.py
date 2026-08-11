from retrieval.retriever import retrieve_documents


def main():

    query = "What are the symptoms of dengue?"

    results = retrieve_documents(query)

    print("\n" + "=" * 80)

    for i, doc in enumerate(results, start=1):

        print(f"\nResult {i}")
        print("-" * 80)
        print(f"Source : {doc.metadata['source']}")
        print(f"Page   : {doc.metadata['page']}")

        print("\nContent:\n")
        print(doc.page_content)


if __name__ == "__main__":
    main()