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
    output = generator(
        prompt,
        max_new_tokens=256,
        do_sample=False   # VERY IMPORTANT → deterministic
    )
    return output[0]["generated_text"]
