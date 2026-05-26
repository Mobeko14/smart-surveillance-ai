import cv2

class MotionDetector:
    def __init__(self, min_area=2000):
        self.min_area = min_area
        self.back_sub = cv2.createBackgroundSubtractorMOG2(
            history=500,
            varThreshold=50,
            detectShadows=False
        )

    def detect(self, frame):
        fg_mask = self.back_sub.apply(frame)

        # Nettoyage du bruit
        fg_mask = cv2.GaussianBlur(fg_mask, (5, 5), 0)
        _, thresh = cv2.threshold(fg_mask, 200, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        motion_detected = False

        for contour in contours:
            if cv2.contourArea(contour) < self.min_area:
                continue

            motion_detected = True
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return frame, motion_detected
