# Import necessary libraries
import streamlit as st  # for building a web app interface
from dotenv import load_dotenv  # for loading environment variables

# Load environment variables from a .env file
load_dotenv()

import os  # for interacting with the operating system
import google.generativeai as genai  # for using Google Gemini's generative AI

from youtube_transcript_api import YouTubeTranscriptApi  # for extracting YouTube video transcripts

# Configure Google Gemini with API key from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the prompt for the summarization model
prompt = """You are a YouTube Video Summarizer. Your role is to take the full transcript of a video and create a clear, structured summary that captures the key points, major insights, and important details in a concise yet comprehensive manner.

Requirements for the Summary:

Begin with an overview of the video's main topic and purpose.
Outline each major point covered in the video, emphasizing key takeaways and actionable insights.
If applicable, include any examples, case studies, or anecdotes mentioned to illustrate key concepts.
End with a conclusion that recaps the primary message or final thoughts from the video.
Present this summary in bullet points, using simple language that anyone can understand, focusing on clarity and thoroughness.
"""

# Function to extract transcript data from YouTube videos
def extract_transcript_details(youtube_video_url):
    try:
        # Get the video ID from the YouTube URL
        video_id = youtube_video_url.split("=")[1]
        
        # Fetch the transcript using the video ID
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        # Combine transcript text pieces into a single string
        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        # Raise any exceptions that occur
        raise e

# Function to generate summary based on transcript and prompt using Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    # Initialize the generative model
    model = genai.GenerativeModel("gemini-pro")
    # Generate content by appending the transcript to the prompt
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Streamlit UI section for the app
st.title("YouTube Transcript to Detailed Notes Converter")  # App title
youtube_link = st.text_input("Enter YouTube Video Link:")  # Input field for YouTube link

# Display thumbnail if a YouTube link is entered
if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

# Button to generate detailed notes
if st.button("Get Detailed Notes"):
    # Extract transcript from the provided YouTube link
    transcript_text = extract_transcript_details(youtube_link)

    # If transcript is extracted successfully, generate summary
    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)
