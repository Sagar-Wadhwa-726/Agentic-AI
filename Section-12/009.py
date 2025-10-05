"""profiling tells the time spent in each function"""

"""non-daemon thread : here the main thread will not exit until the another non-daemon thread has exited whereas in case of the daemon thread, the daemon thread will exit as soon as the main thread exits"""

import threading
import time

def monitor_tea_temp():
    while True:
        print("Monitoring the temperature . . .")
        time.sleep(2)

t = threading.Thread(target=monitor_tea_temp)
t.start()

print("Main program done !")

# use this for profiling:
# python -m cProfile -s time .\009.py
