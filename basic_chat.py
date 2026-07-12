import requests

def ask(prompt):
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.1:8b",
            "messages": [{"role": "user", "content": prompt}],
            "stream": False
        }
    )
    return response.json()["message"]["content"]

print(ask("What is 2 + 2? Answer in one word."))
print(ask("Write a Python function to reverse a string."))