import os
import re
import streamlit as st
from dotenv import load_dotenv
from google import genai
from youtube_transcript_api import YouTubeTranscriptApi

# ---------------- Load API Key ---------------- #

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="AI YouTube Summarizer",
    page_icon="🎥",
    layout="centered"
)

st.title("🎥 AI YouTube Video Summarizer")
st.write("Paste a YouTube video URL and get an AI-generated summary.")

# ---------------- URL Input ---------------- #

video_url = st.text_input("Enter YouTube Video URL")

# ---------------- Function ---------------- #

def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, url)

    if match:
        return match.group(1)

    return None

# ---------------- Button ---------------- #

if st.button("Generate Summary"):

    if not video_url:

        st.warning("Please enter a YouTube URL.")

    else:

        video_id = extract_video_id(video_url)

        if video_id:

            st.success("Valid YouTube URL")

            try:

                # Get Transcript
                transcript = YouTubeTranscriptApi().fetch(video_id)

                transcript_text = ""

                for line in transcript:
                    transcript_text += line.text + " "

                st.subheader("📄 Transcript")

                st.text_area(
                    "Transcript",
                    transcript_text,
                    height=250
                )

                prompt = f"""
You are an expert AI assistant.

Summarize the following YouTube transcript.

Provide:

1. Short Summary
2. Key Points
3. Important Learnings
4. Action Items

Transcript:

{transcript_text}
"""

                with st.spinner("Generating AI Summary..."):

                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=prompt
                    )

                st.subheader("🤖 AI Summary")

                st.write(response.text)

            except Exception as e:

                st.error("Transcript not available for this video.")
                st.exception(e)

        else:

            st.error("Invalid YouTube URL.")