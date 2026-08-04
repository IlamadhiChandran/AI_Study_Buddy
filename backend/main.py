from fastapi import FastAPI, UploadFile, File
import shutil

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to AI Study Buddy 🚀"}

@app.get("/about")
def about():
    return {
        "project": "AI Study Buddy",
        "version": "1.0",
        "developer": "Ilamadhi"
    }


@app.post("/upload")
def upload_pdf(file: UploadFile = File(...)):
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "PDF uploaded successfully!",
        "filename": file.filename
    }