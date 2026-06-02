import time
import threading

def func(sec):
    print(f"Takes {sec} seconds.")
    time.sleep(sec)

start = time.perf_counter()
func(4)
func(3)
func(1)
end = time.perf_counter()
print(f"Without multithreading, Taken total {end-start} seconds.")

start = time.perf_counter()
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[3])
t3 = threading.Thread(target=func, args=[1])
t1.start()
t2.start()
t3.start()
end = time.perf_counter()

# if we want to wait until a thread is executed use .join()
# t1.join()
# t2.join()
# t3.join()

print(f"With multithreading, Taken {end-start} secons.")
