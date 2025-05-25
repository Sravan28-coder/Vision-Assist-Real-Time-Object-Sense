Vision Assist – Real-Time Object Sense-
Vision Assist is a Python-based Flask API that uses Google Gemini 1.5 Flash API to analyze the surrounding environment in real-time via your webcam. 
It captures video frames, generates a description using Gemini AI, and speaks the result aloud using text-to-speech.

🚀 Features
📷 Captures real-time video frames using OpenCV
🧠 Sends frames to Gemini 1.5 Flash API for visual analysis
🔊 Converts the AI-generated description to speech using pyttsx3
🌐 Simple REST API using Flask

📦 Tech Stack
Python 3
Flask
OpenCV
pyttsx3 (text-to-speech)
Gemini API

Project Structure:
vision-assist/
├── app.py                  # Flask app with routes
├── gemini_utils.py         # Handles Gemini 1.5 API image analysis
├── speak.py                # Text-to-speech logic
├── video_capture.py        # Webcam frame capture
├── venv/                   # (optional) virtual environment
└── .gitignore              # Ignores venv, __pycache__, etc.
