import cv2
from detector import MultiplePersonDetector

def test_single_person():
    detector = MultiplePersonDetector()

    frame = cv2.imread("tests/image1.png")

    result = detector.detect(frame)

    assert result["person_count"] == 1
    assert result["violation"] is False


def test_multiple_persons():
    detector = MultiplePersonDetector()

    frame = cv2.imread("tests/image2.png")

    # Run multiple times because violation
    # depends on consecutive detections

    for _ in range(5):
        result = detector.detect(frame)

    assert result["person_count"] >= 2
    assert result["violation"] is True