# from fastapi import FastAPI, UploadFile, File
# from pydantic import BaseModel
# from main import workflow_node
# import shutil

# app = FastAPI()

# class RagQuestion(BaseModel):
#     question: str


# @app.get("/")
# def home():
#     return {"message": "API is running"}


# @app.post("/upload")
# def upload_pdf(file: UploadFile = File(...)):

#     with open("uploaded.pdf", "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     return {"message": "PDF uploaded successfully"}


# @app.post("/rag")
# def rag_node(state: RagQuestion):

#     answer = workflow_node(state.question)

#     return {
#         "question": state.question,
#         "answer": answer
#     } 

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from Rag_full.main import workflow_node, process_pdf
import shutil

app = FastAPI()


class RagQuestion(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/upload")
def upload_pdf(file: UploadFile = File(...)):

    file_path = "uploaded.pdf"

    # Save uploaded PDF
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process PDF (chunking + embeddings + vector DB)
    process_pdf(file_path)

    return {"message": "PDF uploaded and processed successfully"}


@app.post("/rag")
def rag_node(state: RagQuestion):

    answer = workflow_node(state.question)

    return {
        "question": state.question,
        "answer": answer
    }