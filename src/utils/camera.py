import cv2

class Camera:
    def __init__(self, source=0, width=960, height=720):
        self.source = source
        self.width = width
        self.height = height
        self.cap = None

    def start(self):
        self.cap = cv2.VideoCapture(self.source)

        if not self.cap.isOpened():
            raise Exception("Impossible d'ouvrir la camera")

        # 🔹 Forcer la resolution (important pour Haar)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

        # 🔹 Stabilisation auto-exposition (optionnel mais utile)
        self.cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.75)

        print(f"Camera demarree en {self.width}x{self.height}")

    def read(self):
        if self.cap is None:
            raise Exception("Camera non initialisee")

        ret, frame = self.cap.read()

        if not ret:
            return False, None

        return True, frame

    def stop(self):
        if self.cap:
            self.cap.release()
            cv2.destroyAllWindows()
            print("Camera arretee")
