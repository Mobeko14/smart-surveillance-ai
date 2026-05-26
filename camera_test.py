import cv2
import face_recognition
from modules.face_recognizer import FaceRecognizer
import time


def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Impossible d'ouvrir la caméra")
        return

    recognizer = FaceRecognizer(tolerance=0.5)

    last_process_time = 0
    face_locations = []
    results = []

    print("Caméra démarrée...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        current_time = time.time()

        # 🔹 Ne faire la reconnaissance que toutes les 1.5 secondes
        if current_time - last_process_time > 1.5:

            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small = small_frame[:, :, ::-1]

            face_locations = face_recognition.face_locations(rgb_small)

            if face_locations:
                results = recognizer.recognize(small_frame, face_locations)
            else:
                results = []

            last_process_time = current_time

        for ((top, right, bottom, left), (name, confidence)) in zip(face_locations, results):

            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            if name == "admin":
                color = (0, 0, 255)
            else:
                color = (0, 255, 255)

            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, f"{name} ({confidence}%)",
                        (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        color, 2)

        cv2.imshow("Smart Surveillance", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
