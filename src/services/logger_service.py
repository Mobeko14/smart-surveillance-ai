import os
from datetime import datetime


class AccessLogger:

    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.log_dir = os.path.join(base_dir, "logs")
        self.log_file = os.path.join(self.log_dir, "access.log")

        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def log_access(self, name, confidence):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if name == "ADMIN":
            status = "ACCES AUTORISE"
        else:
            status = "ACCES REFUSE"

        log_entry = f"{timestamp} | {name} | {confidence}% | {status}\n"

        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(log_entry)