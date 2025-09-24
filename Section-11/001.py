"""Concurrency and parallelism

Concurrency - Making tea for some time and for some other time putting this task on hold (for a fraction of second) and then working on some another task like replying to some message.

CPU context switches between multiple tasks.  

In parallelism - there are multiple cores and each core does its task. Parallelism is good in the case of multiple cores.

In multiple core functionality - if we have to process a video, each core will process some chunk of the video, but if one core is lazy it won't return the response, because of which the whole process can't be finished, after it is finished then it will take processing time to combine the results of all the cores. In this case parallelism might not be the best case becuase concurrency will just make one core finish the task completely in X amount of time.

Concurrency - threading.Thread
asyncio

Parallelism - multiprocessing.Process
concurrent.futures.ProcessPoolExecutor

"""

import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking order for #{i}")

        # like a complex processing which takes time
        time.sleep(1)

def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(2)

# 2 threads will be created, which will execute their own methods
# setting up target of the thread, it will return some result
# threading.Thread = take_orders()
# threading.Thread = brew_chai()

order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

# multithreading - 
order_thread.start()
brew_thread.start()

# wait for both threads to finish
# join simply means the thread when finished has to come back and report the work done
order_thread.join()
brew_thread.join()

print(f"All orders taken and chai brewed !")