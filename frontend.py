import streamlit as st
import requests

st.title("📄 PDF RAG Chatbot")

API_URL = "http://127.0.0.1:8000"

# -------------------------
# Upload PDF
# -------------------------
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:

    files = {
        "file": (uploaded_file.name, uploaded_file, "application/pdf")
    }

    response = requests.post(
        f"{API_URL}/upload",
        files=files
    )

    if response.status_code == 200:
        st.success("✅ PDF uploaded and processed successfully!")
    else:
        st.error("❌ Upload failed")


# -------------------------
# Ask Question
# -------------------------
question = st.text_input("Ask a question from the PDF")

if st.button("Ask"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        response = requests.post(
            f"{API_URL}/rag",
            json={"question": question}
        )

        if response.status_code == 200:
            data = response.json()
            st.write("### Answer")
            st.write(data["answer"])
        else:
            st.error("❌ Failed to get answer")