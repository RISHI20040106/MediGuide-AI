"""
splitter.py

Splits LangChain Document objects into smaller chunks
for embedding and retrieval.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Split documents into smaller overlapping chunks.

    Args:
        documents (list):
            List of LangChain Document objects.

    Returns:
        list:
            List of chunked Document objects.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    chunks = text_splitter.split_documents(documents)

    print(f"Total chunks created: {len(chunks)}")

    return chunks