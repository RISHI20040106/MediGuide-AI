"""
retriever.py

Performs semantic search on the ChromaDB vector database
and returns the most relevant document chunks.
"""

from retrieval.vector_store import load_vector_database

# ==========================
# Configuration
# ==========================
TOP_K_RESULTS = 3


def retrieve_documents(query: str):
    """
    Retrieve the most relevant document chunks for a user query.

    Args:
        query (str): User's question.

    Returns:
        list: List of relevant LangChain Document objects.
    """

    # Load the existing vector database
    vector_db = load_vector_database()

    # Create a retriever
    retriever = vector_db.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": TOP_K_RESULTS,
        "fetch_k": 10,
        "lambda_mult": 0.7,
    },
)

    # Retrieve relevant documents
    results = retriever.invoke(query)

    print("\nRelevant documents retrieved successfully.")
    print(f"Total Results: {len(results)}")

    return results