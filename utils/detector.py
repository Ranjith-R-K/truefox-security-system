from ultralytics import YOLO

model = YOLO("models/weapon_model.pt")

def detect_weapon(frame):
    results = model(frame)
    return results