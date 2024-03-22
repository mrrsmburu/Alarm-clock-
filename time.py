
import time
import datetime

def set_alarm():
    while True:
        try:
            user_time = input("Enter a time for the alarm in the following format (H:M:S AM/PM): ")
            alarm_time = datetime.datetime.strptime(user_time, "%I:%M:%S %p")
            break
        except ValueError:
            print("Invalid time format. Please try again.\n")
      while True:
        now = datetime.datetime.now().strftime("%I:%M:%S %p")
        if now == alarm_time.strftime("%I:%M:%S %p"):
            print("Time to wake up!")
            break
        else:
            print(now)
            
        time.sleep(1)

set_alarm() 