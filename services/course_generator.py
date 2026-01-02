import json
from services.llm import generate_text

def generate_course(tutor, language, level):
    prompt = f"""
Generate a structured language course in JSON only.

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
    start = raw.find("{")
    return json.loads(raw[start:])
