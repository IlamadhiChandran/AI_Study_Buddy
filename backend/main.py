from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.upload import router as upload_router
from api.chat import router as chat_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(upload_router)
app.include_router(chat_router)

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