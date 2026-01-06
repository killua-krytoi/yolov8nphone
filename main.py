from ultralytics import YOLO
import cv2
import time

# Загружаем YOLOv8 nano (легкая модель, автоматически скачивается)
model = YOLO("yolov8n.pt")

# Настройки
CELL_PHONE_CLASS_ID = 67   # COCO: cell phone
WARNING_SECONDS = 5        # через сколько секунд выдаем предупреждение
start_time = None

# Камера
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Детекция
    results = model(frame)

    phone_detected = False

    # Проходим по всем объектам
    for box in results[0].boxes:
        if int(box.cls[0]) == CELL_PHONE_CLASS_ID:
            phone_detected = True
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]

            # Рисуем рамку и подпись
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, f"PHONE {conf:.2f}", (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Логика таймера
    if phone_detected:
        if start_time is None:
            start_time = time.time()
        elif time.time() - start_time > WARNING_SECONDS:
            print("⚠️ WARNING: Телефон слишком долго в кадре!")
    else:
        start_time = None

    # Показ кадра
    cv2.imshow("Phone Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
