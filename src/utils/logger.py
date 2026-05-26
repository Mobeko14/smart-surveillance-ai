import os
from datetime import datetime

LOG_DIR = "logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def log_event(message):
    filename = os.path.join(LOG_DIR, "events.log")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")
