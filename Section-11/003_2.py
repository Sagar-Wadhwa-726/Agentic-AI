from multiprocessing import Process
import time

def crunch_number():
    print(f"Started the conunt process. . .")
    count = 0
    for _ in range(100_000_000):
        count+=1
    print(f"Ended the count process. . .")

if __name__ == "__main__":
    start = time.time()
    p1 = Process(target=crunch_number)
    p2 = Process(target=crunch_number)

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    

# if main method not provided, the new process does not know the entry point of
