import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from pypdf import PdfReader

# Load API Key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("Ab8RN6L48eeuneKUFUW1Ub6PicugHJgpExCpQKTai0n0Luq7Lw")
)

# Page Settings
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get AI feedback.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    st.success("✅ Resume uploaded successfully!")

    if st.button("Analyze Resume"):

        prompt = f"""
You are a professional HR recruiter.

Analyze the following resume and provide:

1. Resume Score out of 100
2. Strengths
3. Weaknesses
4. Missing Skills
5. ATS Improvement Tips
6. Final Suggestions

Resume:

{resume_text}
"""

        with st.spinner("🤖 AI is analyzing your resume..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

        st.subheader("📊 Analysis Report")
        st.write(response.text)