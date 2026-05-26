import face_recognition
import os
import numpy as np


class FaceRecognizer:
    def __init__(self, tolerance=0.5, min_confidence=60):
        self.tolerance = tolerance
        self.min_confidence = min_confidence

        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        known_dir = os.path.join(base_dir, "known_faces")

        self.known_encodings = []

        for file in os.listdir(known_dir):
            if file.lower().endswith((".jpg", ".png", ".jpeg")):
                image_path = os.path.join(known_dir, file)
                image = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image)

                if encodings:
                    self.known_encodings.append(encodings[0])

        print("ADMIN chargé avec", len(self.known_encodings), "échantillons")

    def recognize(self, frame, face_locations):

        rgb_frame = frame[:, :, ::-1]

        encodings = face_recognition.face_encodings(
            rgb_frame,
            face_locations
        )

        results = []

        for encoding in encodings:

            if not self.known_encodings:
                results.append(("INCONNU", 0))
                continue

            face_distances = face_recognition.face_distance(
                self.known_encodings,
                encoding
            )

            best_match_index = np.argmin(face_distances)
            distance = face_distances[best_match_index]

            confidence = round((1 - distance) * 100, 2)

            # 🎯 CONDITION IMPORTANTE
            if distance < self.tolerance and confidence >= self.min_confidence:
                results.append(("ADMIN", confidence))
            else:
                results.append(("INCONNU", confidence))

        return results
