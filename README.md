# Multiple Person Detection

## Overview

This project detects multiple persons in front of a webcam using MediaPipe Face Detection and OpenCV.

The system is designed for online proctoring and monitoring applications where only one person is allowed in the camera frame. If more than one person is detected for a specified number of consecutive frames, a violation is triggered.

---

## Features

* Real-time face detection using MediaPipe
* Counts the number of persons in the frame
* Detects multiple persons
* Triggers violation after consecutive detections
* REST API using Flask
* Live webcam testing utility
* Configurable detection parameters
* Image-based unit testing with PyTest

---

## Project Structure

```text
multiple_person_detection/
│
├── app.py                     # Flask API
├── detector.py                # Detection logic
├── config.py                  # Configuration settings
├── test_detector.py           # Webcam testing script
├── test_image_detection.py    # Image-based unit tests
├── tests/
│   ├── image1.png             # Single-person test image
│   └── image2.png             # Multiple-person test image
├── requirements.txt           # Dependencies
└── output/                    # Output folder
```

---

## Requirements

* Python 3.10+
* Webcam

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Dependencies

```text
Flask
OpenCV
MediaPipe
NumPy
PyTest
```

---

## Configuration

Edit `config.py` to customize the detector settings:

```python
MAX_ALLOWED_PERSONS = 1
VIOLATION_AFTER_FRAMES = 5
MIN_DETECTION_CONFIDENCE = 0.6
MIN_FACE_AREA = 0.02
CAMERA_INDEX = 0
```

### Parameter Description

| Parameter                | Description                                  |
| ------------------------ | -------------------------------------------- |
| MAX_ALLOWED_PERSONS      | Maximum allowed persons in frame             |
| VIOLATION_AFTER_FRAMES   | Consecutive frames required before violation |
| MIN_DETECTION_CONFIDENCE | Minimum confidence for face detection        |
| MIN_FACE_AREA            | Filters tiny/background faces                |
| CAMERA_INDEX             | Webcam index                                 |

---

## Run Webcam Detection

Start real-time detection using your webcam:

```bash
python test_detector.py
```

### Example Output

```json
{
  "person_count": 2,
  "violation": true
}
```

---

## Run Flask API

Start the API server:

```bash
python app.py
```

Server URL:

```text
http://127.0.0.1:5000
```

### API Endpoint

```http
GET /detect
```

### Example Response

```json
{
  "person_count": 1,
  "violation": false
}
```

---

## Run Unit Tests

This project includes image-based unit tests to verify the detection logic without requiring a webcam.

```bash
pytest test_image_detection.py
```

### Expected Output

```text
========================
2 passed
========================
```

### Test Cases

#### Single Person Test

Input:

```text
tests/image1.png
```

Expected:

```json
{
  "person_count": 1,
  "violation": false
}
```

#### Multiple Persons Test

Input:

```text
tests/image2.png
```

Expected:

```json
{
  "person_count": 2,
  "violation": true
}
```

---

## Detection Logic

1. Capture webcam frame.
2. Convert frame from BGR to RGB.
3. Detect faces using MediaPipe Face Detection.
4. Calculate face area.
5. Ignore tiny/background faces using `MIN_FACE_AREA`.
6. Count valid faces.
7. If person count exceeds the allowed limit:

   * Increment violation counter.
8. If violation counter reaches threshold:

   * Trigger violation.
9. Return detection results.

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
* Face recognition for candidate verification

---

## Technologies Used

* Python
* OpenCV
* MediaPipe
* Flask
* NumPy
* PyTest

---

## Author

**Preethi G N**

MCA Student
Surana College, Bangalore
