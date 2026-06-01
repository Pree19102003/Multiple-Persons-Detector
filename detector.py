import cv2
import mediapipe as mp

from config import (
    MAX_ALLOWED_PERSONS,
    VIOLATION_AFTER_FRAMES,
    MIN_DETECTION_CONFIDENCE,
    MIN_FACE_AREA
)


class MultiplePersonDetector:

    def __init__(self):
        self.face_detector = mp.solutions.face_detection.FaceDetection(
            model_selection=0,
            min_detection_confidence=MIN_DETECTION_CONFIDENCE
        )

        self.violation_counter = 0

    def detect(self, frame):
        """
        Detect faces and determine if multiple people are present.
        """

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.face_detector.process(rgb_frame)

        person_count = 0

        if results.detections:

            for detection in results.detections:

                bbox = detection.location_data.relative_bounding_box

                face_area = bbox.width * bbox.height

                # Ignore very small faces
                if face_area >= MIN_FACE_AREA:
                    person_count += 1

        # Consecutive-frame threshold logic
        if person_count > MAX_ALLOWED_PERSONS:
            self.violation_counter += 1
        else:
            self.violation_counter = 0

        violation = (
            self.violation_counter >= VIOLATION_AFTER_FRAMES
        )

        return {
            "person_count": person_count,
            "violation": violation
        }