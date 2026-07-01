import os
import time
import tempfile

import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import pyttsx3

from dotenv import load_dotenv
from langchain_groq import ChatGroq

# ==========================
# Load Environment Variables
# ==========================
load_dotenv()

# ==========================
# Initialize Groq
# ==========================
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)

# ==========================
# Initialize Text-to-Speech
# ==========================
engine = pyttsx3.init()

engine.setProperty("rate", 170)

# ==========================
# Load Whisper Model
# ==========================
print("Loading Whisper Model...")
model = whisper.load_model("base")

print("✅ Whisper Loaded Successfully!")

print("=" * 60)
print("🤖 AI Voice Assistant")
print("=" * 60)

while True:

    input("\nPress ENTER to start recording...")

    duration = 8
    fs = 16000

    print("\n🎤 Get Ready...")
    time.sleep(2)

    print("🎤 Speak Now...")

    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype="int16",
        device=2      # Realtek Microphone
    )

    sd.wait()

    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    temp.close()

    write(temp.name, fs, recording)

    print("\n📝 Converting Speech to Text...")

    result = model.transcribe(temp.name)

    question = result["text"].strip()

    print("\nWhisper Heard:")
    print(question)

    if question == "":
        print("\n⚠️ No speech detected.")
        try:
            os.remove(temp.name)
        except:
            pass
        continue

    if question.lower() in ["exit", "quit", "stop"]:
        print("\n👋 Goodbye!")
        break

    print("\n🤖 Thinking...")

    response = llm.invoke(question)

    answer = response.content

    print("\n==============================")
    print("🧑 You :", question)
    print("🤖 AI  :", answer)
    print("==============================")

    engine.say(answer)
    engine.runAndWait()

    try:
        os.remove(temp.name)
    except:
        pass