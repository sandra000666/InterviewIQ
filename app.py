from flask import Flask, render_template, request, jsonify
import json
import ollama

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/category")
def category():
    return render_template("category.html")


@app.route("/interview")
def interview():
    category = request.args.get("category", "General Programming")

    with open("questions.json", "r", encoding="utf-8") as file:
        all_questions = json.load(file)

    questions = [
        q for q in all_questions
        if q.get("category") == category
    ]

    return render_template(
        "interview.html",
        questions=questions,
        category=category
    )
@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/evaluate", methods=["POST"])
def evaluate():

    data = request.get_json()

    question = data["question"]
    answer = data["answer"]
    difficulty = data.get("difficulty", "Beginner")

    prompt = f"""
You are an AI programming interview evaluator.

Evaluate the candidate's answer based mainly on technical correctness.

Important evaluation rules:
- Focus on whether the answer is correct and relevant to the programming question.
- Do not give a low score only because of grammar, spelling, or simple English mistakes.
- Give a higher score when the candidate understands the main concept, even if the explanation is short.
- Give a lower score when the answer is technically incorrect, unrelated, or missing important concepts.
- Keep your feedback short and easy to understand.
- Do not be overly strict with beginner-level questions.

Question difficulty:
{difficulty}

Question:
{question}

Candidate answer:
{answer}

Give ONLY these four items:

Score: X/10
Mistake: one short sentence about the main missing or incorrect point
Better answer: one or two short sentences
Feedback: one short encouraging sentence

Difficulty rules:
- Beginner: Focus on understanding the basic concept. Do not require advanced details.
- Easy: Expect a clear basic explanation with a simple example when appropriate.
- Medium: Expect a reasonably complete technical explanation.
- Hard: Expect accurate comparison, reasoning, or important technical details.
- Advanced: Expect a strong understanding of the major concepts mentioned in the question.

Scoring guide:
9-10 = Excellent and technically accurate
7-8 = Good with minor missing details
5-6 = Partially correct
3-4 = Mostly incorrect or incomplete
1-2 = Incorrect or unrelated

Do not give explanations, reasoning, or extra text.
"""
    response = ollama.chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        think=False,
        stream=False
    )

    return jsonify({
        "feedback": response["message"]["content"]
    })


if __name__ == "__main__":
    app.run(debug=True)