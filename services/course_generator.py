from services.llm import generate_text

def generate_course(tutor, language, level):
    prompt = f"""
      You are a professional language tutor.

      Generate a short course using EXACT markers.

      FORMAT (DO NOT CHANGE):

      COURSE_TITLE: <title>

      MODULE: <module title>
      LESSON: <lesson title>
      CONTENT:
      <lesson content>

      RULES:
      - Use simple language
      - Be culturally accurate
      - 1 module, 2 lessons only
      - No markdown
      - No explanations

      Language: {language}
      Level: {level}
      Tutor: {tutor['fullname']}
      Teaching specialities: {tutor['teaching_specialities']}
      Learning style: {tutor['learning_styles']}
      """

    raw = generate_text(prompt)
    print(raw)

    return parse_course(raw)


def parse_course(text: str):
    lines = [l.strip() for l in text.splitlines() if l.strip()]

    course = {
        "title": "",
        "modules": []
    }

    current_module = None
    current_lesson = None
    collecting_content = False

    for line in lines:
        if line.startswith("COURSE_TITLE:"):
            course["title"] = line.replace("COURSE_TITLE:", "").strip()

        elif line.startswith("MODULE:"):
            current_module = {
                "module_title": line.replace("MODULE:", "").strip(),
                "lessons": []
            }
            course["modules"].append(current_module)

        elif line.startswith("LESSON:"):
            current_lesson = {
                "lesson_title": line.replace("LESSON:", "").strip(),
                "content": ""
            }
            current_module["lessons"].append(current_lesson)
            collecting_content = False

        elif line.startswith("CONTENT:"):
            collecting_content = True

        elif collecting_content and current_lesson:
            current_lesson["content"] += line + " "

    return course
