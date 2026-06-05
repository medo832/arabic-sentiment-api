from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# Load the pre-trained sentiment analysis model
model = pipeline(
    "sentiment-analysis",
    model="CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment"
)
# Define API endpoints
@app.get("/")
def home():
    return {"message": "API is working"}

# Endpoint to analyze sentiment of the input text
@app.post("/analyze")
def analyze(text: str):
    result = model(text)
    return {"text": text, "result": result}