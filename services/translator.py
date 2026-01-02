from transformers import pipeline

translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M"
)

LANG_MAP = {
    "yoruba": "yor_Latn",
    "zulu": "zul_Latn",
    "hausa": "hau_Latn",
    "igbo": "ibo_Latn",
    "swahili": "swh_Latn"
}

def translate(text: str, language: str) -> str:
    code = LANG_MAP.get(language.lower())
    if not code:
        return text
    return translator(text, tgt_lang=code)[0]["translation_text"]
