import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load API Key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("Ab8RN6L48eeuneKUFUW1Ub6PicugHJgpExCpQKTai0n0Luq7Lw")
)

# Page Settings
st.set_page_config(
    page_title="Adil AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Adil AI Assistant")
st.write("Ask me anything!")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
question = st.chat_input("Type your message...")

if question:

    # Show User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Loading Spinner
    with st.spinner("🤖 AI is thinking..."):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )

        answer = response.text

    # Save AI Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # Show AI Response
    with st.chat_message("assistant"):
        st.markdown(answer)