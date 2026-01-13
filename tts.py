import requests
from client import client

voice_id = "KHmfNHtEjHhLK9eER20w"
url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

def call_tts(text: str) -> bytes:
    headers = {
        "xi-api-key": client.token_tts,
        "Content-Type": "application/json",
        "Accept": "audio/wav"
    }

    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2"
    }

    r = requests.post(url, headers=headers, json=payload)

    if r.status_code != 200:
        raise Exception(f"TTS error {r.status_code}: {r.text}")

    return r.content
