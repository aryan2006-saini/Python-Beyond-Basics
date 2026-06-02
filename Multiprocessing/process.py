from multiprocessing import Process
import time

def work():
    time.sleep(3)
    print("Finished")

if __name__ == "__main__":
    p = Process(target=work)
    p.start()
    print("Waiting...")
    p.join()
    print("Done")