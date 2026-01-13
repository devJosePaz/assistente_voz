from dotenv import load_dotenv
import os

load_dotenv()

class Client:
    token_llm = os.getenv("TOKEN_LLM")
    token_tts = os.getenv("TOKEN_TTS")

client = Client()
