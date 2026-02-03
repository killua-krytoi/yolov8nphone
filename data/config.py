from ultralytics import YOLO
from gpiozero import LED, Buzzer
import cv2

led = LED(14)
buzzer = Buzzer(21)

model = YOLO("yolov8n.pt")

CELL_PHONE_CLASS_ID = 0 #67-mobiel, 0-mens

WARNING_SECONDS = 0
FRAMES = 10
frame_count = 0
start_time = None

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
results = model(frame, imgsz=320, classes=[CELL_PHONE_CLASS_ID], verbose=False)

def tune_cv():
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)