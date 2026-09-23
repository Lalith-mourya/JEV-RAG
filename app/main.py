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
async def upload(file : UploadFile=File(...)):  # File(...) is used to accept the multi from data
    if file.filename.endswith(".txt"):
        text = await file.read() # this return byte format , so we are converting this as the str
        content = text.decode("utf-8")
        return {
            "filename" : file.filename,
            "valid": True,
            "content": content
        }
    elif file.filename.endswith(".pdf"):
        return{
            "filename": file.filename,
            "valid":True
        }
    else:
        raise HTTPException(status_code=400,detail="This format is not supported")
        

