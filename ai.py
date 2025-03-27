import google.generativeai as genai
import pyttsx3  # For text-to-speech

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

if __name__ == "__main__":
    print("🎓 Welcome to EduHelper (Gemini Edition with Voice)\n")

    context = """
    The water cycle describes how water moves through Earth's systems: evaporation from oceans and lakes,
    condensation into clouds, precipitation as rain or snow, and collection back into bodies of water.
    It is a continuous process powered by the sun.
    """

    question = input("🤔 Your Question: ")
    answer = ask_edu_question(question, context)

    print(f"\n✅ Answer: {answer}")
    
    # 🔊 Speak the answer
    print("🔈 Speaking answer...")
    engine.say(answer)
    engine.runAndWait()
