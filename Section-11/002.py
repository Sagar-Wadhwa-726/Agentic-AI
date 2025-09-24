from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of {name} chai served !")
    time.sleep(3)
    print(f"End of {name} chai served !")

if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}", ))
        for i in range(3)
    ]

    # Start all process
    for p in  chai_makers:
        p.start() 

    # Wait for all the process to complete
    for p in chai_makers:
        p.join()

    print("All Chai served !")