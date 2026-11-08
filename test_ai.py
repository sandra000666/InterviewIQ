import ollama

response = ollama.chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "user",
            "content": "Answer in one short sentence: What is a variable in programming?"
        }
    ]
)

print(response["message"]["content"])
