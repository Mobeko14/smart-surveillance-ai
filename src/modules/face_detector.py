import face_recognition
import cv2


class FaceDetector:

    def detect(self, frame):
        rgb_frame = frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_frame)

        face_detected = len(face_locations) > 0

        return frame, face_detected, face_locations
