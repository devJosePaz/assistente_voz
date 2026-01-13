import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from transcription import transcription_audio

CHANNELS = 1
SAMPLERATE = 44100
AUDIO_FILE = "audio.wav"

def record_and_transcribe() -> str:
    frames = []

    def callback(indata, frames_count, time, status):
        frames.append(indata.copy())

    print("\n🎙️ Pressione ENTER para iniciar a gravação")
    input()

    print("⏺️ Gravando... pressione ENTER para parar")

    with sd.InputStream(
        samplerate=SAMPLERATE,
        channels=CHANNELS,
        callback=callback
    ):
        input()

    audio = np.concatenate(frames, axis=0)
    write(AUDIO_FILE, SAMPLERATE, audio)

    return transcription_audio(AUDIO_FILE)
