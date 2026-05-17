from ultralytics import YOLO


model = YOLO("yolov8n.pt")

model.train(
    data="datasets/clean_weapon_dataset/data.yaml",epochs=20,imgsz=640,batch=8,
    name="weapon_detector")