import streamlit as st
from transformers import pipeline

HF_TOKEN = st.secrets["HF_TOKEN"]

@st.cache_resource
def load_translator():
    return pipeline(
        "translation",
        model="facebook/nllb-200-distilled-600M",
        token=HF_TOKEN
    )

translator = load_translator()

LANG_MAP = {
    "yoruba": "yor_Latn",
    "zulu": "zul_Latn",
    "hausa": "hau_Latn",
    "igbo": "ibo_Latn",
    "swahili": "swh_Latn"
}


def translate(text, lang):
    code = LANG_MAP.get(lang.lower())
    if not code:
        return text
    return translator(text, tgt_lang=code)[0]["translation_text"]
