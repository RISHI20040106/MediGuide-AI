"""
==========================================================
MediGuide AI
Medical Guideline Intelligence Platform

Part 1
----------------------------------------------------------
✓ Imports
✓ Page Configuration
✓ Session State
✓ Custom CSS
✓ Professional Header
✓ Premium Sidebar
==========================================================
"""

# ==========================================================
# Imports
# ==========================================================

import streamlit as st
from pathlib import Path

from rag.chain import ask_question


# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="MediGuide AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ==========================================================
# Session State
# ==========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==========================================================
# Custom CSS
# ==========================================================

st.markdown("""
<style>

/* ------------------------------------------------ */
/* Hide Streamlit Menu */
/* ------------------------------------------------ */

#MainMenu{
    visibility:hidden;
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* ------------------------------------------------ */
/* Main Background */
/* ------------------------------------------------ */

.stApp{
    background:#F5F7FA;
}

/* ------------------------------------------------ */
/* Sidebar */
/* ------------------------------------------------ */

section[data-testid="stSidebar"]{

    background:#FFFFFF;

    border-right:1px solid #E5E7EB;

}

/* ------------------------------------------------ */
/* Header */
/* ------------------------------------------------ */

.main-title{

    font-size:42px;

    font-weight:700;

    color:#2563EB;

    margin-bottom:0;

}

.sub-title{

    font-size:18px;

    color:#6B7280;

    margin-top:-8px;

}

/* ------------------------------------------------ */
/* Sidebar Cards */
/* ------------------------------------------------ */

.sidebar-card{

    background:white;

    border:1px solid #E5E7EB;

    border-radius:14px;

    padding:16px;

    margin-bottom:12px;

    transition:0.25s;

}

.sidebar-card:hover{

    border-color:#2563EB;

    box-shadow:0px 4px 12px rgba(0,0,0,0.08);

}

.card-title{

    font-size:18px;

    font-weight:600;

    color:#1F2937;

}

.card-subtitle{

    font-size:13px;

    color:#6B7280;

    margin-top:4px;

}

/* ------------------------------------------------ */
/* Chat Messages */
/* ------------------------------------------------ */

div[data-testid="stChatMessage"]{

    border-radius:14px;

    border:1px solid #E5E7EB;

    background:white;

    padding:12px;

    margin-bottom:14px;

}

/* ------------------------------------------------ */
/* Chat Input */
/* ------------------------------------------------ */

div[data-testid="stChatInput"]{

    border-radius:14px;

}

/* ------------------------------------------------ */
/* Scrollbar */
/* ------------------------------------------------ */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:#C5C5C5;

    border-radius:20px;

}

</style>
""", unsafe_allow_html=True)


# ==========================================================
# Header
# ==========================================================

st.markdown(
    """
    <div class="main-title">
        🩺 MediGuide AI
    </div>

    <div class="sub-title">
        Medical Guideline Intelligence Platform
    </div>
    """,
    unsafe_allow_html=True,
)

st.write(
    "Search and explore trusted medical guidelines using AI."
)

st.divider()


# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.markdown("## 📖 Guidelines")

    guidelines = [

        ("🦟", "Dengue"),

        ("🩺", "Hypertension"),

        ("🦠", "COVID-19"),

    ]

    for icon, disease in guidelines:

        st.markdown(
            f"""
            <div class="sidebar-card">

                <div class="card-title">

                    {icon} {disease}

                </div>

                <div class="card-subtitle">

                    WHO Guideline

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True,
):
        st.session_state.messages = []
        st.rerun()
 
    st.divider()

    st.markdown("### ℹ About")

    st.info(
        """
MediGuide AI retrieves answers only from the uploaded medical guideline documents.

It does not use external medical knowledge.
"""
    )

    st.divider()

    st.warning(
        """
**Disclaimer**

This application is intended for educational purposes only.

Always consult a qualified healthcare professional before making medical decisions.
"""
    )



# ==========================================================
# Display Previous Messages
# ==========================================================
if len(st.session_state.messages) == 0:

    st.info(
        """
### 👋 Welcome to MediGuide AI

Ask questions from trusted medical guideline documents.

#### Available Guidelines

- 🦟 Dengue
- 🩺 Hypertension
- 🦠 COVID-19

Start by typing your question below.
"""
    )


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        # Display sources only for assistant messages
        if message["role"] == "assistant":

            if "sources" in message:

                with st.expander("📚 Sources", expanded=False):

                    displayed = set()

                    for doc in message["sources"]:

                        source = doc.metadata.get(
                            "source",
                            "Unknown"
                        )

                        page = doc.metadata.get(
                            "page",
                            0
                        )

                        if isinstance(page, int):
                            page += 1

                        filename = Path(source).stem

                        key = (filename, page)

                        if key not in displayed:

                            displayed.add(key)

                            st.markdown(
                                f"""
**📄 {filename}**

Page **{page}**
"""
                            )




      # ==========================================================
# Chat Input
# ==========================================================

question = st.chat_input(
    "Ask about a medical guideline..."
)


# ==========================================================
# Generate AI Response
# ==========================================================

if question:

    # ------------------------------------------
    # Save User Question
    # ------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    # ------------------------------------------
    # Display User Message
    # ------------------------------------------

    with st.chat_message("user"):

        st.markdown(question)

   
    # Assistant Response
    

    with st.chat_message("assistant"):

        with st.spinner("🩺 Searching trusted medical guidelines..."):

            try:

                result = ask_question(question)

            except Exception as e:

                st.error(f"An error occurred:\n\n{e}")

                st.stop()

        # ------------------------------------------
        # Extract Answer & Documents
        # ------------------------------------------

        answer = result["answer"]

        documents = result["documents"]

        # ------------------------------------------
        # Display Answer
        # ------------------------------------------

        st.markdown(answer)

        # ------------------------------------------
        # Display Sources
        # ------------------------------------------

    if documents:

     with st.expander("📚 Sources", expanded=False):

        displayed = set()

        for doc in documents:

            source = doc.metadata.get("source", "Unknown")
            page = doc.metadata.get("page", 0)

            if isinstance(page, int):
                page += 1

            filename = Path(source).stem
            key = (filename, page)

            if key not in displayed:

                displayed.add(key)

                st.markdown(
                    f"""
📄 **{filename}**

📑 Page **{page}**
"""
                )        
              
                       
              

 # ------------------------------------------
 # Save Assistant Response
 # ------------------------------------------

    st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "sources": documents,
            }
        )  


# ==========================================================
# Extra Chat Spacing
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)


# ==========================================================
# Footer
# ==========================================================

st.markdown(
    """
    <style>
    .custom-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: white;
        border-top: 1px solid #E5E7EB;
        text-align: center;
        padding: 10px;
        font-size: 13px;
        color: #6B7280;
        z-index: 998;
    }
    </style>

    <div class="custom-footer">
        🩺 MediGuide AI | Powered by LangChain • ChromaDB • Ollama • Llama 3.2
    </div>
    """,
    unsafe_allow_html=True,
)