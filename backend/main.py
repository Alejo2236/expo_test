from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_questions = [
    {"id": 1, "question": "2 + 2 = ?", "options": ["3", "4"], "answer": "4"},
    {"id": 2, "question": "Capital of France?", "options": ["Paris", "Berlin"], "answer": "Paris"},
]

@app.get("/questions")
def get_questions():
    return fake_questions
