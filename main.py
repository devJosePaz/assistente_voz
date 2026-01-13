import time
import sys

from stt import record_and_transcribe
from llm import call_llm
from tts import call_tts
from audio_player import play_mp3

TTS_FILE = "tts.mp3"


def type_print(text: str, delay: float = 0.015):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def main():
    # STT
    text = record_and_transcribe()

    print("\n📝 Você disse:")
    type_print(text)

    # LLM
    llm_response = call_llm(text)

    print("\n🤖 Resposta:")
    type_print(llm_response)

    # TTS
    audio_bytes = call_tts(llm_response)
    with open(TTS_FILE, "wb") as f:
        f.write(audio_bytes)

    print("\n🔊 Falando...\n")
    play_mp3(TTS_FILE)


if __name__ == "__main__":
    main()
