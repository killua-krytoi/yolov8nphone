from data.config import (CLASS_ID,
        FRAMES,
        cap,
        results,
        ret)
from data.main_logic import phone_detected_run
def main():
    from data.config import tune_cv
    tune_cv()
    while True:
        if not ret:
            break
        from data.config import frame_count
        frame_count += 1
        if frame_count % FRAMES != 0:
            continue
        phone_detected = False
        for box in results[0].boxes:
            if int(box.cls[0]) == CLASS_ID:
                phone_detected = True
                break
        if phone_detected:
            phone_detected_run()
        else:
            start_time = None
    cap.release()
if __name__ == "__main__":
    main()