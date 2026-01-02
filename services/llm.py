import os
import streamlit as st
from transformers import pipeline

HF_TOKEN = st.secrets["HF_TOKEN"]

@st.cache_resource
def load_generator():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        token=HF_TOKEN
    )

generator = load_generator()

def generate_text(prompt: str) -> str:
    result = generator(prompt, max_length=512)
    return result[0]["generated_text"]
