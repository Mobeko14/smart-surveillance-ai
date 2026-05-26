import os
import cv2
from datetime import datetime

DATA_DIR = "data"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def save_snapshot(frame):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(DATA_DIR, f"intrusion_{timestamp}.jpg")
    cv2.imwrite(filename, frame)
    return filename
