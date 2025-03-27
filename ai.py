import streamlit as st
import google.generativeai as genai
import pyttsx3  # For text-to-speech
import tempfile
import os

# 🔑 Replace with your Gemini API key
API_KEY = "AIzaSyDD4P-p1Vvhnng1XcLxsVrSl3DUzRRoG_A"

# 🔧 Configure Gemini
genai.configure(api_key=API_KEY)

# ✅ Use a supported model name
model = genai.GenerativeModel('models/gemini-1.5-pro-001')
chat = model.start_chat()

# 🎤 Initialize the TTS engine
engine = pyttsx3.init()

def ask_edu_question(question, context):
    prompt = f"""
    You are an educational assistant. Help a student by answering clearly based on this study material.

    📚 Study Material:
    {context}

    ❓ Question:
    {question}

    🎯 Answer in a student-friendly way:
    """
    response = chat.send_message(prompt)
    return response.text

def text_to_speech(text):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        filename = fp.name
    engine.save_to_file(text, filename)
    engine.runAndWait()
    return filename

# 🎛️ Streamlit UI
st.set_page_config(page_title="EduHelper (Gemini Edition)", page_icon="🎓")
st.title("🎓 EduHelper - Gemini + Voice Assistant")
st.markdown("Ask a question based on the provided study material below:")

default_context = """
The water cycle describes how water moves through Earth's systems: evaporation from oceans and lakes,
condensation into clouds, precipitation as rain or snow, and collection back into bodies of water.
It is a continuous process powered by the sun.
"""

context = st.text_area("📚 Study Material", value=default_context, height=150)
question = st.text_input("❓ Ask Your Question")

if st.button("🔍 Get Answer"):
    if question.strip():
        with st.spinner("Thinking..."):
            answer = ask_edu_question(question, context)
            st.success("✅ Answer:")
            st.markdown(answer)

            # 🔈 Generate and play speech
            audio_path = text_to_speech(answer)
            st.audio(audio_path, format="audio/mp3")
            os.remove(audio_path)
    else:
        st.warning("Please enter a question.")

