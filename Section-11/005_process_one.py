import threading
import time

def cpu_heave():
    print(f"Crunching some numbers . . .")
    total = 0
    for i in range(10**7):
        total += 1
    print(f"Done !")

start = time.time()
threads = [threading.Thread(target=cpu_heave) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Time taken : {time.time()-start:.2f} seconds")