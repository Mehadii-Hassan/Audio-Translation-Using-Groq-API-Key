import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Transcribe a sample audio file
with open("Recording.mp3", "rb") as audio_file:
    output = client.audio.transcriptions.create(
        model="whisper-large-v3",
        file=audio_file
    )

print("Transcription:", output.text)
