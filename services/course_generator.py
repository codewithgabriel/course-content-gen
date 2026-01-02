import json
import re
from services.llm import generate_text

JSON_REGEX = re.compile(r"\{.*\}", re.DOTALL)

def extract_json(text: str):
    match = JSON_REGEX.search(text)
    if not match:
        raise ValueError("No JSON object found in model output")
    return json.loads(match.group())

def generate_course(tutor, language, level):
    prompt = f"""
      TASK:
      Return ONLY valid JSON.
      Do NOT explain.
      Do NOT add markdown.

      Language: {language}
      Level: {level}
      Tutor: {tutor['fullname']}
      Teaching specialities: {tutor['teaching_specialities']}
      Learning style: {tutor['learning_styles']}

      JSON SCHEMA:
      {{
        "title": "string",
        "modules": [
          {{
            "module_title": "string",
            "lessons": [
              {{
                "lesson_title": "string",
                "content": "string"
              }}
            ]
          }}
        ]
      }}
      """

    raw = generate_text(prompt)

    try:
        return extract_json(raw)
    except Exception:
        # One automatic retry (important)
        raw_retry = generate_text(prompt)
        return extract_json(raw_retry)
