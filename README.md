<h1 align="center">🎤 Audio Translator</h1>

<p align="center">
  A Flask web app that transcribes speech from audio files using <b>Whisper-large-v3</b> and translates it into any language with <b>Llama 3.1 via Groq API</b>.
  <br><br>
  Upload an audio file 🎧 ➝ Get instant transcription 📝 ➝ Translate into your chosen language 🌍
</p>

<hr>

<h2>🚀 Features</h2>
<ul>
  <li>🎙️ <b>Speech-to-Text</b>: Transcribe audio using <code>Whisper-large-v3</code>.</li>
  <li>🌐 <b>Multi-Language Translation</b>: Translate into any language with <code>Llama 3.1</code>.</li>
  <li>⚡ <b>Groq-Powered</b>: Leverages high-speed Groq API for real-time inference.</li>
  <li>💻 <b>Web UI</b>: Upload files easily via Flask + HTML frontend.</li>
  <li>🐍 <b>Demo Script</b>: Run <code>demo.py</code> to test transcription locally.</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>

<pre>
├── app.py              # Flask application
├── demo.py             # Sample script to transcribe audio
├── index.html          # Web frontend (templates)
├── static/             # Static assets (recording file)
├── requirements.txt    # Dependencies
├── .gitignore
└── README.md
</pre>

<hr>

<h2>⚙️ Installation</h2>

<pre>
# Clone the repository
git clone https://github.com/your-username/groq-whisper-translator.git
cd groq-whisper-translator

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt
</pre>

<hr>

<h2>🔑 Setup</h2>
<p>Create a <code>.env</code> file in the project root and add:</p>

<pre>
GROQ_API_KEY=your_groq_api_key_here
</pre>

<hr>

<h2>▶️ Run the App</h2>

<pre>
# Start the Flask app
python app.py
</pre>

<p>Open in browser: 👉 <a href="http://127.0.0.1:8080" target="_blank">http://127.0.0.1:8080</a></p>

<hr>

<h2>🧪 Run Demo Script</h2>

<pre>
python demo.py
</pre>

<p>Make sure you have an audio file named <code>Recording.mp3</code> in the root folder.</p>

<hr>

<h2>📸 Screenshots</h2>

<p align="center">
  <img src="https://via.placeholder.com/800x400?text=Upload+Audio+UI" alt="Web UI Screenshot">
</p>


<hr>

<h2>🙌 Credits</h2>

<p>
Created by <strong>Mehedi Hassan</strong> using <code>Groq API</code> (LLaMA 3.1).  
</p>

<hr>

<p align="center">⭐ Star this repo if you enjoy this!</p>
