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
    page_title="AI PDF Chatbot",
    page_icon="📄"
)

st.title("📄 AI PDF Chatbot")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)

if uploaded_file:

    reader = PdfReader(uploaded_file)

    pdf_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pdf_text += text

    st.success("✅ PDF uploaded successfully!")

    question = st.text_input("Ask a question about the PDF")

    if st.button("Ask AI"):

        prompt = f"""
        PDF Content:

        {pdf_text}

        Question:
        {question}
        """

        with st.spinner("🤖 AI is reading the PDF..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

        st.subheader("AI Answer")
        st.write(response.text)