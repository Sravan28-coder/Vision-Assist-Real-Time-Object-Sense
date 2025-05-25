import cv2
import time

def capture_frames(duration=3):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Cannot open camera")

    start_time = time.time()
    frames = []

    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if not ret:
            continue

        _, buffer = cv2.imencode(".jpg", frame)
        frames.append(buffer.tobytes())

    cap.release()
    return frames
