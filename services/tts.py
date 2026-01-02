from TTS.api import TTS
import os
import uuid
HF_TOKEN = os.getenv("HF_TOKEN")
tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/your_tts")

AUDIO_DIR = "audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

def generate_audio(text: str) -> str:
    file_path = f"{AUDIO_DIR}/{uuid.uuid4()}.wav"
    tts.tts_to_file(text=text, file_path=file_path)
    return file_path
