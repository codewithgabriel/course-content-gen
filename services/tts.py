from TTS.api import TTS
import streamlit as st
import uuid
import os

@st.cache_resource
def load_tts():
    return TTS(model_name="tts_models/multilingual/multi-dataset/your_tts")

tts = load_tts()

AUDIO_DIR = "audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

def generate_audio(text):
    path = f"{AUDIO_DIR}/{uuid.uuid4()}.wav"
    tts.tts_to_file(text=text, file_path=path)
    return path
