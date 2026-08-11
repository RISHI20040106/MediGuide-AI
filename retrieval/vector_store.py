"""
vector_store.py

Loads the existing ChromaDB vector database.
"""

from langchain_chroma import Chroma

from ingestion.embedding import get_embedding_model

# ==========================
# Configuration
# ==========================
VECTOR_DB_PATH = "vectorstore/chroma_db"


def load_vector_database():
    """
    Load the existing ChromaDB vector database.

    Returns:
        Chroma: Loaded vector database.
    """

    embedding_model = get_embedding_model()

    vector_db = Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embedding_model,
    )

    print("Vector database loaded successfully.")

    return vector_db