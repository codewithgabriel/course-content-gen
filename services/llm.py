from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
import os
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"
HF_TOKEN = os.getenv("HF_TOKEN")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
)

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=900,
    temperature=0.7,
    token=HF_TOKEN

)

def generate_text(prompt: str) -> str:
    return generator(prompt)[0]["generated_text"]
