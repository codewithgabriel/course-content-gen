import json
from services.llm import generate_text

def generate_course(tutor, language, level):
    prompt = f"""
You are a professional language tutor.

Generate a structured course in JSON only.

Language: {language}
Level: {level}
Tutor name: {tutor['fullname']}
Teaching specialities: {tutor['teaching_specialities']}
Learning style: {tutor['learning_styles']}

STRICT JSON FORMAT:
{{
  "title": "...",
  "modules": [
    {{
      "module_title": "...",
      "lessons": [
        {{
          "lesson_title": "...",
          "content": "..."
        }}
      ]
    }}
  ]
}}
"""

    raw = generate_text(prompt)
    json_start = raw.find("{")
    clean = raw[json_start:]

    return json.loads(clean)
