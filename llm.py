import requests
from client import client

def call_llm(text: str) -> str:
    url = "https://router.huggingface.co/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {client.token_llm}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "openai/gpt-oss-120b:fastest",
        "messages": [
            {
                "role": "system",
                "content": "Você é um assistente que gera respostas curtas, objetivas e claras, adequadas para conversão em áudio (TTS). Evite totalmente listas longas, excesso de exemplos e linguagem acadêmica."
            },

            {
                "role": "user",
                "content": text

            }
        ]
    }

    r = requests.post(url, headers=headers, json=body)

    if r.status_code != 200:
        raise Exception(f"LLM error: {r.status_code}: {r.text}")

    data = r.json()

    return data["choices"][0]["message"]["content"]
