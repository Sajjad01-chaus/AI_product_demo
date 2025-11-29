from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# Using a small pipeline for quick loading
classifier = pipeline("sentiment-analysis")

@app.get("/predict")
def predict(text: str):
    return classifier(text)
