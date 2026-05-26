import cv2
import face_recognition
from modules.face_recognizer import FaceRecognizer
from services.logger_service import AccessLogger
from services.email_service import EmailService
import time
import os
from datetime import datetime
import threading


# =========================
# UTILITAIRES
# =========================

def draw_datetime(frame):
    now = datetime.now()
    cv2.putText(frame, now.strftime("%Y-%m-%d %H:%M:%S"),
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2)


def save_unknown(frame):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    capture_dir = os.path.join(base_dir, "captures")

    if not os.path.exists(capture_dir):
        os.makedirs(capture_dir)

    filename = f"intrus_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    filepath = os.path.join(capture_dir, filename)

    cv2.imwrite(filepath, frame)
    return filepath


def send_email_async(email_service, image_path):
    thread = threading.Thread(
        target=email_service.send_intrusion_alert,
        args=(image_path,),
        daemon=True
    )
    thread.start()


# =========================
# MAIN
# =========================

def main():

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Impossible d'ouvrir la caméra")
        return

    recognizer = FaceRecognizer(tolerance=0.65, min_confidence=50)
    logger = AccessLogger()
    email_service = EmailService()

    recognition_interval = 1.0
    last_recognition_time = 0

    tracker = None
    tracking = False
    tracked_name = None
    tracked_confidence = 0

    unknown_streak = 0
    alarm_active = False
    last_email_time = 0
    email_cooldown = 20

    print("Caméra démarrée (mode performance + tracking)...")

    while True:

        ret, frame = cap.read()
        if not ret:
            break

        current_time = time.time()

        # =============================
        # 🔵 MODE TRACKING
        # =============================
        if tracking and tracker is not None:

            success, box = tracker.update(frame)

            if success:
                x, y, w, h = [int(v) for v in box]

                if tracked_name == "ADMIN":
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 255)

                label = f"{tracked_name} ({tracked_confidence}%)"

                cv2.rectangle(frame, (x, y),
                              (x + w, y + h),
                              color, 2)

                cv2.putText(frame, label,
                            (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8, color, 2)

            else:
                tracking = False
                tracker = None

        # =============================
        # 🟢 MODE RECONNAISSANCE
        # =============================
        if not tracking and current_time - last_recognition_time > recognition_interval:

            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small = small_frame[:, :, ::-1]

            face_locations = face_recognition.face_locations(
                rgb_small,
                model="hog"
            )

            if face_locations:

                results = recognizer.recognize(rgb_small, face_locations)
                name, confidence = results[0]

                (top, right, bottom, left) = face_locations[0]
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # 🔥 Démarrage tracking
                tracker = cv2.legacy.TrackerCSRT_create()
                tracker.init(frame, (left, top, right - left, bottom - top))

                tracking = True
                tracked_name = name
                tracked_confidence = confidence

                logger.log_access(name, confidence)

                # =============================
                # 🔐 LOGIQUE D'ALARME CORRIGÉE
                # =============================
                if name == "INCONNU":
                    unknown_streak += 1

                    if unknown_streak >= 3:
                        alarm_active = True

                else:  # ADMIN reconnu
                    unknown_streak = 0
                    alarm_active = False  # 🔥 Désactivation propre

            last_recognition_time = current_time

        # =============================
        # 🚨 AFFICHAGE ALARME
        # =============================
        if alarm_active:

            cv2.putText(frame, "ALERTE INTRUS",
                        (50, 80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.2,
                        (0, 0, 255),
                        3)

            if current_time - last_email_time > email_cooldown:
                image_path = save_unknown(frame)
                send_email_async(email_service, image_path)
                last_email_time = current_time

        draw_datetime(frame)

        cv2.imshow("Smart Surveillance - Tracking + Logs", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()