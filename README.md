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

## 🖼 Sample Screenshots

### Homepage

<img width="100%" alt="Homepage" src="https://github.com/user-attachments/assets/79cb443c-e334-4f19-a0dd-e132c7ae1b2c" />

### Questions Page

<img width="100%" alt="Questions Page" src="https://github.com/user-attachments/assets/166bdc78-4cdf-4473-8f72-e25ca7b8e966" />

### Results Page

<img width="100%" alt="Results Page" src="https://github.com/user-attachments/assets/318de14a-41da-4b50-a83a-f10cc6d03f3f" />

## ⚠️ Notes

* First run downloads the AI model (~250MB)
* English language only
* Not a clinical or medical assessment

## 📄 License

MIT License
