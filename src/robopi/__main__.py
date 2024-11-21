from flask import Flask, Response
import cv2
import numpy as np

from . import camera


app = Flask(__name__)

def generate_frames():
    while True:
        frame = camera.get_array()
        _, buffer = cv2.imencode(".jpg", frame)
        frame_bytes = buffer.tobytes()
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n")

@app.route("/video_feed")
def video_feed():
    return Response(generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/")
def index():
    return '<html><body><h1>Raspberry Pi Camera Stream</h1><img src="/video_feed"></body></html>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8765)