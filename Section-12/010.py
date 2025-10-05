"""in this code in production race condition can occur since we are not using any locks or mutex, hence the final value of the variable chai_stock might fluctuate"""

import threading

chai_stock = 0

def restock():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1

threads = [threading.Thread(target=restock) for _ in range(2)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Chai Stock : ", chai_stock)