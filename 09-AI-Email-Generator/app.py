import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load API Key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")

st.set_page_config(
    page_title="AI Email Generator",
    page_icon="📧",
    layout="centered"
)

st.title("📧 AI Email Generator")

purpose = st.text_input("Purpose of Email")
recipient = st.text_input("Recipient")

tone = st.selectbox(
    "Select Tone",
    ["Professional", "Friendly", "Formal", "Casual"]
)

details = st.text_area("Additional Details")

if st.button("Generate Email"):

    prompt = f"""
Write a {tone} email.

Purpose:
{purpose}

Recipient:
{recipient}

Additional Details:
{details}

Generate:
- Subject
- Email Body
- Closing
"""

    with st.spinner("Generating Email..."):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

    st.subheader("Generated Email")

    st.write(response.text)