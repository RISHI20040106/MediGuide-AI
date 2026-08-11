"""
indexer.py

Creates a ChromaDB vector database from the medical guideline PDFs.
"""

from langchain_chroma import Chroma

from ingestion.loader import load_documents
from ingestion.splitter import split_documents
from ingestion.embedding import get_embedding_model
from ingestion.cleaner import clean_documents


# ==========================
# Configuration
# ==========================
VECTOR_DB_PATH = "vectorstore/chroma_db"


def create_vector_database():
    """
    Create and store document embeddings in ChromaDB.

    Returns:
        Chroma: Initialized Chroma vector database.
    """

    print("=" * 60)
    print("Starting Document Indexing...")
    print("=" * 60)

    # Step 1: Load documents
    documents = load_documents()

    documents = clean_documents(documents)

    # Step 2: Split documents into chunks
    chunks = split_documents(documents)

    # Step 3: Load embedding model
    embedding_model = get_embedding_model()

    # Step 4: Create and persist ChromaDB
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=VECTOR_DB_PATH,
    )

    print("\n" + "=" * 60)
    print("Indexing Completed Successfully!")
    print("=" * 60)
    print(f"Documents Loaded : {len(documents)}")
    print(f"Chunks Created   : {len(chunks)}")
    print(f"Database Saved   : {VECTOR_DB_PATH}")

    return vector_db