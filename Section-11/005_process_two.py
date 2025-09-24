from multiprocessing import Process 
import time

def cpu_heave():
    print(f"Crunching some numbers . . .")
    total = 0
    for i in range(10**8):
        total += 1
    print(f"Done !")

if __name__ == "__main__":
    start = time.time()
    processes = [Process(target=cpu_heave) for _ in range(2)]
    [t.start() for t in processes]
    [t.join() for t in processes]

    print(f"Time taken : {time.time()-start:.2f} seconds")