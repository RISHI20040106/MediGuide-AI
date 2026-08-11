"""
embedding.py

Loads the Hugging Face embedding model used to convert
document chunks and user queries into vector embeddings.
"""

from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    """
    Load and return the Hugging Face embedding model.

    Returns:
        HuggingFaceEmbeddings: Embedding model instance.
    """

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )

    return embedding_model