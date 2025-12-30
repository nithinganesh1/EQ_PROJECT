# 🧠 Emotional Intelligence (EQ) Assessment Tool

A simple AI-powered web application to assess Emotional Intelligence (EQ) using scenario-based questions and NLP analysis.

## ✨ Features

* AI-based emotion analysis (HuggingFace Transformers)
* Scenario-based EQ assessment
* 5 EQ categories:

  * Self Awareness
  * Emotional Regulation
  * Conflict Handling
  * Empathy
  * Resilience
* Radar chart visualization

## 🛠 Tech Stack

* **Backend**: Python, Flask
* **AI/NLP**: HuggingFace Transformers, PyTorch
* **Frontend**: HTML,Chart.js
* **Model**: emotion-english-distilroberta-base

## 📊 Scoring

Each answer is scored using:

* Emotion analysis – 40%
* EQ keyword matching – 40%
* Response depth – 20%

Score range: **0–10** per EQ category.

## 🚀 Run Locally

```bash
git clone https://github.com/nithinganesh1/EQ_PROJECT.git
cd EQ_PROJECT
pip install -r requirements.txt
python app.py
```

Open in browser:

```
http://localhost:5000
```

## 📁 Project Structure

```
EQ_PROJECT/
├── ai/
│   └── eq_engine.py
├── templates/
│   ├── index.html
│   ├── questions.html
│   └── result.html
├── app.py
├── requirements.txt
└── README.md
```

## ⚠️ Notes

* First run downloads the AI model (~250MB)
* English language only
* Not a clinical or medical assessment

##
