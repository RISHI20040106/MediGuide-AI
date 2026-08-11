"""
loader.py

Loads all PDF documents from the data folder and converts them
into LangChain Document objects.
"""

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_documents(data_folder: str = "data") -> list:
    """
    Load all PDF files from the specified folder.

    Args:
        data_folder (str): Path to the folder containing PDF files.

    Returns:
        list: A list of LangChain Document objects.

    Raises:
        FileNotFoundError: If the data folder does not exist.
        ValueError: If no PDF files are found.
    """

    data_path = Path(data_folder)

    # Check if data folder exists
    if not data_path.exists():
        raise FileNotFoundError(
            f"Data folder '{data_folder}' does not exist."
        )

    # Find all PDF files
    pdf_files = list(data_path.glob("*.pdf"))

    if not pdf_files:
        raise ValueError(
            f"No PDF files found in '{data_folder}'."
        )

    documents = []

    # Load each PDF
    for pdf_file in pdf_files:
        print(f"Loading: {pdf_file.name}")

        loader = PyPDFLoader(str(pdf_file))
        docs = loader.load()

        documents.extend(docs)

    print(f"\nSuccessfully loaded {len(pdf_files)} PDF file(s).")
    print(f"Total pages loaded: {len(documents)}")

    return documents