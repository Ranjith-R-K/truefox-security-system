from datetime import datetime

def log_detection():
    with open("results/logs/detection_log.txt", "a") as file:
        file.write(f"Weapon detected at {datetime.now()}\n")