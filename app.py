import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from groq import Groq

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static"


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        language = request.form["language"]
        file = request.files["file"]

        if file:
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # --- Transcribe audio using Groq Whisper ---
            with open(filepath, "rb") as audio_file:
                transcript = client.audio.transcriptions.create(
                    model="whisper-large-v3",
                    file=audio_file
                )

            # --- Translate text using Llama via Groq ---
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": f"You will be provided with a sentence in English, and your task is to translate it into {language}"},
                    {"role": "user", "content": transcript.text}
                ],
                temperature=0,
                max_tokens=256
            )

            return jsonify({"translation": response.choices[0].message.content})

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
