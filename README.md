# Multiple Person Detection

## Overview

This project detects multiple persons in front of a webcam using MediaPipe Face Detection and OpenCV.

The system is designed for online proctoring and monitoring applications where only one person is allowed in the camera frame.

---

## Features

* Real-time face detection
* Counts the number of persons in the frame
* Detects multiple persons
* Triggers violation after consecutive detections
* REST API using Flask
* Live webcam testing utility

---

## Project Structure

```text
multiple_person_detection/
│
├── app.py                 # Flask API
├── detector.py            # Detection logic
├── config.py              # Configuration settings
├── test_detector.py       # Webcam testing script
├── requirements.txt       # Dependencies
└── output/                # Output folder
```

---

## Requirements

* Python 3.10+
* Webcam

### Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies:

```text
Flask
OpenCV
MediaPipe
NumPy
```

---

## Configuration

Edit `config.py`:

```python
MAX_ALLOWED_PERSONS = 1
VIOLATION_AFTER_FRAMES = 5
MIN_DETECTION_CONFIDENCE = 0.6
MIN_FACE_AREA = 0.02
CAMERA_INDEX = 0
```

---

## Run Webcam Detection

```bash
python test_detector.py
```

Output:

```json
{
  "person_count": 2,
  "violation": true
}
```

---

## Run Flask API

```bash
python app.py
```

Server:

```text
http://127.0.0.1:5000
```

### API Endpoint

```text
GET /detect
```

Example Response:

```json
{
  "person_count": 1,
  "violation": false
}
```

---

## Detection Logic

1. Capture webcam frame.
2. Convert frame to RGB.
3. Detect faces using MediaPipe.
4. Filter tiny faces using area threshold.
5. Count valid faces.
6. If count > 1:

   * Increase violation counter.
7. If counter reaches threshold:

   * Trigger violation.

---

## Example Outputs

### Single Person

```json
{
  "person_count": 1,
  "violation": false
}
```

### Multiple Persons

```json
{
  "person_count": 2,
  "violation": true
}
```

---

## Future Improvements

* Face tracking
* Person re-identification
* Mobile phone detection
* Eye gaze monitoring
* Screenshot capture on violation
* Violation logging database
* Audio monitoring

---

## Author

Preethi G N

MCA Student
Surana College, Bangalore
