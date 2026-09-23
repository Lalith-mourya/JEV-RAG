from fastapi import FastAPI,UploadFile,File,HTTPException
from pydantic import BaseModel
from schema.response import QuestionRequest
app = FastAPI()


@app.get("/")
def give():
    return "RAG is running"

@app.post("/user_question")
def ques(request:QuestionRequest):
    return request.question

@app.post("/upload")
def upload(file : UploadFile=File(...)):
    if file.filename.endswith(".pdf") or file.filename.endswith(".txt"):
        return {
            "filename" : file.filename,
            "valid": True
        }
    else:
        raise HTTPException(status_code=400,detail="This format is not supported")
        


