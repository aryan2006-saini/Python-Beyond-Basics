import threading
import time

def background():
    while True:
        print("Running...")
        time.sleep(3)

t1 = threading.Thread(target=background,daemon=True)
t1.start()
time.sleep(3)
print("Program Ends")