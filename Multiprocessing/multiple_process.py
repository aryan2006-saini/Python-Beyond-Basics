from multiprocessing import Process
import time

def worker(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")

if __name__ == "__main__":

    p1 = Process(target=worker,args=["A"])
    p2 = Process(target=worker,args=["B"])

    p1.start()
    p2.start()

    p1.join()
    p2.join()