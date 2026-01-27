from ultralytics import YOLO
import cv2
import time
from gpiozero import LED, Buzzer
led = LED(14)
buzzer = Buzzer(21)
model = YOLO("yolov8n.pt")
CELL_PHONE_CLASS_ID = 0 #67-mobiel, 0-mens
WARNING_SECONDS = 0
FRAMES = 10
frame_count = 0
start_time = None
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_count +=1
    if frame_count % FRAMES != 0:
        continue
    results = model(frame, imgsz=320, classes=[CELL_PHONE_CLASS_ID], verbose=False)
    phone_detected = False
    for box in results[0].boxes:
        if int(box.cls[0]) == CELL_PHONE_CLASS_ID:
            phone_detected = True
            break
    if phone_detected:
        if start_time is None:
            start_time = time.time()
        elif time.time() - start_time >= WARNING_SECONDS:
            led.on()
            buzzer.beep(0.2, 0.2)
    else:
        start_time = None
        led.off()
        buzzer.off()
cap.release()
led.off()
buzzer.off()
