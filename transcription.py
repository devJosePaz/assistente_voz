import whisper
import os

language = "pt"
model = whisper.load_model("small")
def transcription_audio(audio) -> str:
    transcrition = model.transcribe(audio, fp16=False, language=language)
    result = transcrition["text"]

    return result









    


