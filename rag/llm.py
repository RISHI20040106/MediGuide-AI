"""
llm.py

Loads the Ollama Large Language Model.
"""

from langchain_ollama import ChatOllama

# ==========================================
# Configuration
# ==========================================

MODEL_NAME = "llama3.2:3b"

TEMPERATURE = 0.0

NUM_CTX = 4096        # Context window

NUM_PREDICT = 512     # Maximum response length


def get_llm():
    """
    Load the Ollama LLM.

    Returns:
        ChatOllama
    """

    llm = ChatOllama(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        num_ctx=NUM_CTX,
        num_predict=NUM_PREDICT,
    )

    print(f"LLM Loaded Successfully : {MODEL_NAME}")

    return llm