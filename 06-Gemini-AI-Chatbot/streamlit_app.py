import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("Ab8RN6L48eeuneKUFUW1Ub6PicugHJgpExCpQKTai0n0Luq7Lw")
)

st.set_page_config(
    page_title="Adil AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 Adil AI Assistant")

question = st.text_input("Ask me anything")

if st.button("Send"):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    st.success(response.text)