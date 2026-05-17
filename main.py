import cv2
from utils.detector import detect_weapon
from utils.alert import trigger_alert
from utils.logger import log_detection


cap = cv2.VideoCapture(0)
print("Starting Intelligent Surveillance System...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = detect_weapon(frame)
    annotated_frame = results[0].plot()
    boxes = results[0].boxes

    if len(boxes) > 0:
        trigger_alert()
        log_detection()

    cv2.imshow("AI Security Surveillance", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()