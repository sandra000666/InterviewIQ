# InterviewIQ – AI-Powered Interview Practice

InterviewIQ is an AI-assisted programming interview practice application developed using Python and Flask. It helps users practice programming interview questions, submit answers, receive scores, and improve their responses with AI feedback.

## Features

- Category-based programming interview questions
- Answer submission and evaluation
- AI-powered feedback using Ollama and Qwen3
- Answer scoring and improvement suggestions
- Interview results and performance summary
- Practice history

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Ollama (Qwen3)
- JSON

## Project Structure

```text
InterviewIQ/
├── app.py
├── questions.json
├── test_ai.py
├── .gitignore
├── static/
│   └── style.css
└── templates/
    ├── category.html
    ├── history.html
    ├── index.html
    ├── interview.html
    └── result.html
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/sandra000666/InterviewIQ.git
cd InterviewIQ
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment (Windows)

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install Flask ollama
```

### 5. Download the AI model

Install Ollama and run:

```bash
ollama pull qwen3:8b
```

### 6. Start the application

Start Ollama, then run:

```bash
python app.py
```

Open your browser at:

`http://127.0.0.1:5000`

## Project Purpose

Developed as a PGDCA final-year project to explore Python web development and local AI integration.

## Developer

**Sandra Santhosh**

GitHub: [sandra000666](https://github.com/sandra000666)

## Application Preview

![InterviewIQ Home Page](./InterviewIQ-Home.png)

---

*Built with Python, Flask and a passion for learning AI.*
