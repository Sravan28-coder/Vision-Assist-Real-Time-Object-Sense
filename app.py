from flask import Flask
from gemini_utils import analyze_images_with_gemini
from video_capture import capture_frames
from speak import speak_text

app = Flask(__name__)

@app.route("/")
def home():
    return "Vision Assist API is running!"

@app.route("/analyze", methods=["GET"])
def analyze_env():
    try:
        print("Capturing video frames...")
        frames = capture_frames(duration=3)
        print(f"Captured {len(frames)} frames")

        description = analyze_images_with_gemini(frames)
        print("Gemini Description:", description)

        speak_text(description)

        return {"result": description}
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True)
