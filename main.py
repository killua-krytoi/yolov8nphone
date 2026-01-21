from ultralytics import YOLO
import cv2
import time
model = YOLO("yolov8n.pt")
CELL_PHONE_CLASS_ID = 0 #67-phone, 0-people
WARNING_SECONDS = 5
start_time = None
cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame, verbose=False)
    phone_detected = False
    for box in results[0].boxes:
        if int(box.cls[0]) == CELL_PHONE_CLASS_ID:
            phone_detected = True
            break
    if phone_detected:
        if start_time is None:
            start_time = time.time()
        elif time.time() - start_time >= WARNING_SECONDS:
            print("phone detected for 5 sec")
    else:
        start_time = None
cap.release()