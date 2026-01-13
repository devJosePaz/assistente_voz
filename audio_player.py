import subprocess
import os

def play_mp3(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(path)

    subprocess.run(
        ["ffplay", "-nodisp", "-autoexit", path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
