"""
cleaner.py

Automatically cleans PDF documents by removing repeated
headers, footers, page numbers, empty pages, front matter,
and extra whitespace.
"""

import re
from collections import Counter

MIN_TEXT_LENGTH = 100
REPEAT_THRESHOLD = 3

# Generic keywords usually found in cover pages or front matter
SKIP_KEYWORDS = [
    "table of contents",
    "contents",
    "foreword",
    "preface",
    "acknowledgements",
    "acknowledgments",
    "isbn",
    "copyright",
]


def clean_documents(documents):
    """
    Clean loaded LangChain documents.

    Args:
        documents (list): List of Document objects.

    Returns:
        list: Cleaned Document objects.
    """

    first_lines = []
    last_lines = []

    # ---------------------------------------
    # Detect repeated headers and footers
    # ---------------------------------------
    for doc in documents:

        lines = [
            line.strip()
            for line in doc.page_content.split("\n")
            if line.strip()
        ]

        if lines:
            first_lines.append(lines[0])

        if len(lines) > 1:
            last_lines.append(lines[-1])

    first_counter = Counter(first_lines)
    last_counter = Counter(last_lines)

    cleaned_documents = []

    # ---------------------------------------
    # Clean each document
    # ---------------------------------------
    for doc in documents:

        lines = [
            line.strip()
            for line in doc.page_content.split("\n")
            if line.strip()
        ]

        # Remove repeated header
        if lines and first_counter[lines[0]] >= REPEAT_THRESHOLD:
            lines.pop(0)

        # Remove repeated footer
        if lines and last_counter[lines[-1]] >= REPEAT_THRESHOLD:
            lines.pop()

        text = "\n".join(lines)

        # Remove page numbers
        text = re.sub(r"\bPage\s+\d+\b", "", text, flags=re.IGNORECASE)
        text = re.sub(r"^\d+$", "", text, flags=re.MULTILINE)

        # Normalize spaces
        text = re.sub(r"\s+", " ", text).strip()

        # Skip pages with very little content
        if len(text) < MIN_TEXT_LENGTH:
            continue

        # Skip front matter
        lower_text = text.lower()

        if any(keyword in lower_text for keyword in SKIP_KEYWORDS):
            continue

        doc.page_content = text
        cleaned_documents.append(doc)

    print(f"Documents before cleaning : {len(documents)}")
    print(f"Documents after cleaning  : {len(cleaned_documents)}")

    return cleaned_documents