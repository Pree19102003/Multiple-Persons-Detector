# Maximum number of persons allowed in frame
MAX_ALLOWED_PERSONS = 1

# Number of consecutive frames with multiple persons
# before triggering a violation
VIOLATION_AFTER_FRAMES = 5

# Minimum confidence for face detection
MIN_DETECTION_CONFIDENCE = 0.6

# Minimum face area threshold
# Used to ignore tiny faces (posters/screens/background)
MIN_FACE_AREA = 0.02

# Webcam index
CAMERA_INDEX = 0

# Flask settings
DEBUG = True
HOST = "127.0.0.1"
PORT = 5000