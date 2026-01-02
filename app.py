import streamlit as st
import json
from services.course_generator import generate_course
from services.tts import generate_audio

st.set_page_config(page_title="Tutor Course Generator", layout="wide")

st.title("📚 Tutor Course Generator (Streamlit MVP)")

with open("tutors.json") as f:
    tutors = json.load(f)

tutor_names = [t["fullname"] for t in tutors]
selected = st.selectbox("Select Tutor", tutor_names)

tutor = next(t for t in tutors if t["fullname"] == selected)

st.markdown("### Tutor Profile")
st.write(tutor["about"])

language = st.selectbox(
    "Select Language",
    list(tutor["languages_with_levels"].keys())
)

level = tutor["languages_with_levels"][language]
st.info(f"Level: {level}")

if st.button("Generate Course"):
    with st.spinner("Generating course..."):
        course = generate_course(tutor, language, level)

    st.success(course["title"])

    for module in course["modules"]:
        st.header(module["module_title"])
        for lesson in module["lessons"]:
            st.subheader(lesson["lesson_title"])
            st.write(lesson["content"])

            if st.button(f"🔊 Audio: {lesson['lesson_title']}"):
                audio = generate_audio(lesson["content"])
                st.audio(audio)
