from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from typing import List, TypedDict
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import SentenceTransformersTokenTextSplitter
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langgraph.graph import StateGraph, START, END
import os

load_dotenv()

# -------------------------
# STATE
# -------------------------
class State(TypedDict):
    topic: str
    retriever: List[Document]
    answer: str


# -------------------------
# GLOBAL OBJECTS
# -------------------------
vector_store = None
retriever = None


llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)


# -------------------------
# PDF PROCESSING FUNCTION
# -------------------------
def process_pdf(file_path="uploaded.pdf"):
    global vector_store, retriever

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = SentenceTransformersTokenTextSplitter(
        tokens_per_chunk=200,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    vector_store = FAISS.from_documents(chunks, embeddings)

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 4, "lambda_mult": 0.5}
    )


# -------------------------
# RETRIEVER NODE
# -------------------------
def retriever_node(state: State):

    if retriever is None:
        return {"retriever": []}

    q = state["topic"]
    docs = retriever.invoke(q)

    return {"retriever": docs}


# -------------------------
# HELPER
# -------------------------
def preprocessing(docs: List[Document]):
    context = "\n\n".join(doc.page_content for doc in docs)
    return context


# -------------------------
# GENERATOR NODE
# -------------------------
def generator(state: State):

    prompt = PromptTemplate(
        template="""
You are a helpful AI assistant.

Use ONLY the information provided in the CONTEXT to answer the QUESTION.

Rules:
- Do not use outside knowledge.
- If the answer is not present in the context, say:
  "I don't know based on the provided context."
- Answer clearly and concisely.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
""",
        input_variables=["question", "context"]
    )

    context = preprocessing(state["retriever"])

    chain = prompt | llm

    answer = chain.invoke({
        "question": state["topic"],
        "context": context
    })

    return {"answer": answer.content}


# -------------------------
# LANGGRAPH
# -------------------------
graph = StateGraph(State)

graph.add_node("retriever_node", retriever_node)
graph.add_node("generator", generator)

graph.add_edge(START, "retriever_node")
graph.add_edge("retriever_node", "generator")
graph.add_edge("generator", END)

workflow = graph.compile()


# -------------------------
# MAIN FUNCTION FOR API
# -------------------------
def workflow_node(topic: str):

    result = workflow.invoke({
        "topic": topic,
        "retriever": [],
        "answer": ""
    })

    return result["answer"]