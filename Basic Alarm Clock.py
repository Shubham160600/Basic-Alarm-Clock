import datetime
import time
import winsound  # Only works on Windows

alarm_time = input("Enter alarm time (HH:MM): ")

while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if now == alarm_time:
        print("Wake up!")
        winsound.Beep(1000, 1000)
        break
    time.sleep(10)
