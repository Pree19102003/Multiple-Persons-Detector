from flask import Flask, jsonify
import cv2

from detector import MultiplePersonDetector
from config import CAMERA_INDEX, DEBUG, HOST, PORT

app = Flask(__name__)

detector = MultiplePersonDetector()


@app.route("/")
def home():
    return jsonify({
        "message": "Multiple Person Detection API Running"
    })


@app.route("/detect")
def detect():

    cap = cv2.VideoCapture(CAMERA_INDEX)

    ret, frame = cap.read()

    if not ret:
        cap.release()

        return jsonify({
            "error": "Unable to access webcam"
        }), 500

    result = detector.detect(frame)

    cap.release()

    return jsonify(result)


if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG
    )