import cv2
from picamera2 import Picamera2
from ultralytics import YOLO
from datetime import datetime
import requests
import time

# Load YOLOv8 nano model
model = YOLO("yolov8n.pt")

# Set up Pi Camera
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": "RGB888", "size": (640, 480)}))
picam2.start()

print("Camera started. Press 'q' to quit.")
time.sleep(1)

person_counter = 0
ALERT_THRESHOLD = 90  # ~3 seconds at 30fps


def send_alert():
    timestamp = datetime.now().strftime("%I:%M %p")
    message = f"🚨 INTRUDER DETECTED at {timestamp}"
    print(message)
    try:
        requests.post("https://hacker-console.replit.app/api/alert",
            json={"message": message},
            timeout=3)
    except Exception as e:
        print(f"Alert failed: {e}")


while True:
    frame = picam2.capture_array()
    results = model(frame, verbose=False)

    person_detected = False

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            label = model.names[class_id]
            if label == "person":
                person_detected = True

    if person_detected:
        person_counter += 1
        if person_counter == ALERT_THRESHOLD:
            send_alert()
    else:
        person_counter = 0  # Reset if no person seen

    annotated_frame = results[0].plot()
    annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR)
    cv2.imshow("Boss Detector", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

picam2.stop()
cv2.destroyAllWindows()
