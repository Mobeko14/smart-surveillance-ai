import cv2

class PersonDetector:
    def __init__(self):
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        boxes, weights = self.hog.detectMultiScale(
            gray,
            winStride=(8, 8),
            padding=(8, 8),
            scale=1.05
        )

        persons_detected = False

        for (x, y, w, h) in boxes:
            persons_detected = True
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        return frame, persons_detected
