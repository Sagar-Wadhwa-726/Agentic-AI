"""Daemon threads are the threads which are running in the background and once the main thread exits the daemon threads also automatically shut down. These daemon threads are mostly used for logging and monitoring"""

import threading
import time

def monitor_tea_temp():
    while True:
        print("Monitoring the temperature . . .")
        time.sleep(2)

t = threading.Thread(target=monitor_tea_temp, daemon=True)
t.start()

print("Main program done !")