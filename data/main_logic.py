from config import WARNING_SECONDS
import time

def phone_detected_run():
    from data.config import start_time
    if start_time is None:
        start_time = time.time()
    elif time.time() - start_time >= WARNING_SECONDS:
        print("phone detected")