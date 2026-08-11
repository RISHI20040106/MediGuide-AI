"""
chain.py

Builds the complete RAG pipeline.
"""

from retrieval.retriever import retrieve_documents
from rag.prompt import get_prompt
from rag.llm import get_llm


def ask_question(question: str): 
    """
    Execute the complete RAG pipeline.

    Args:
        question (str): User question.

    Returns:
        str: Generated answer.
    """

    # ==========================
    # Retrieve relevant documents
    # ==========================

    documents = retrieve_documents(question)

    if not documents:
        return "I couldn't find this information in the uploaded medical guidelines."

    # ==========================
    # Build Context
    # ==========================

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    # ==========================
    # Load Prompt
    # ==========================

    prompt = get_prompt()

    formatted_prompt = prompt.format(
        context=context,
        question=question,
    )

    # ==========================
    # Load LLM
    # ==========================

    llm = get_llm()

    # ==========================
    # Generate Answer
    # ==========================

    response = llm.invoke(formatted_prompt)

    return {
    "answer": response.content,
    "documents": documents,
}
