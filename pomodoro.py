import time
import os
from datetime import datetime, timedelta

length = 25
completion_msg = "Hey, time is up!"
say_arg = "say '" + completion_msg + "'"

start = datetime.now()
now = start
stop = now + timedelta(seconds=length * 60)

print("Starting pomodoro of {} minutes at {}".format(length,
      now.strftime("%m/%d/%Y %H:%M")))
while now < stop:
    time.sleep(1)
    now = datetime.now()
    diff = now - start
    # print (now.strftime("%m/%d/%Y %H:%M:%S"), end="", flush=True)
    print(str(diff).split('.')[0], end="", flush=True)
    print("\r", end="", flush=True)
print("Pomodoro completed at {}".format(now.strftime("%H:%M")))
os.system(say_arg)
