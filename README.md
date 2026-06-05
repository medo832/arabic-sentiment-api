# Arabic Sentiment Analysis API

An Arabic sentiment analysis application that classifies Arabic text as **Positive**, **Negative**, or **Neutral** using a pre-trained Arabic BERT model specialized for sentiment analysis. The project includes both a web interface built with Gradio and a REST API built with FastAPI.

## Live Demo

🌐 **Try it here:**

https://medo9090-arabic-sentiment-api.hf.space

---

## Features

* Arabic sentiment analysis
* Pre-trained transformer model
* Interactive web interface using Gradio
* REST API using FastAPI
* Confidence score for each prediction
* Easy deployment on Hugging Face Spaces

---

## Model

This project uses:

`CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment`

Why this model?

* Specifically trained for Arabic language understanding
* Fine-tuned for sentiment analysis
* Supports Arabic dialects and Modern Standard Arabic
* High accuracy without requiring additional training

---

## Project Structure

```text
.
├── app.py        # Gradio web application
├── api.py        # FastAPI backend
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd <repository-name>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install transformers torch gradio fastapi uvicorn
```

---

## Running the Gradio App

Start the web interface:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:7860
```

---

## Running the FastAPI Service

Start the API server:

```bash
uvicorn api:app --reload
```

API will be available at:

```text
http://127.0.0.1:8000
```

Interactive documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "message": "API is working"
}
```

---

### Analyze Sentiment

```http
POST /analyze
```

Parameters:

| Parameter | Type   | Description            |
| --------- | ------ | ---------------------- |
| text      | string | Arabic text to analyze |

Example:

```bash
curl -X POST "http://127.0.0.1:8000/analyze?text=هذا المنتج رائع جدا"
```

Response:

```json
{
  "text": "هذا المنتج رائع جدا",
  "result": [
    {
      "label": "positive",
      "score": 0.99
    }
  ]
}
```

---

## Example Predictions

| Input Text           | Prediction |
| -------------------- | ---------- |
| هذا المنتج رائع جدًا | Positive   |
| الخدمة سيئة للغاية   | Negative   |
| المنتج عادي          | Neutral    |

---

## Technologies Used

* Python
* Transformers
* Hugging Face Models
* Gradio
* FastAPI
* Uvicorn

---

## Author

Mohamed Samir 
