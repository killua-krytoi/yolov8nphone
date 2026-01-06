from ultralytics import YOLO
import cv2
import time
model = YOLO("yolov8n.pt")
CELL_PHONE_CLASS_ID = 67
WARNING_SECONDS = 5
start_time = None
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame)
    phone_detected = False
    for box in results[0].boxes:
        if int(box.cls[0]) == CELL_PHONE_CLASS_ID:
            phone_detected = True
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, f"PHONE {conf:.2f}", (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    if phone_detected:
        if start_time is None:
            start_time = time.time()
        elif time.time() - start_time > WARNING_SECONDS:
            print("⚠️ WARNING")
    else:
        start_time = None
    cv2.imshow("Phone Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()