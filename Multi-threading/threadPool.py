from concurrent.futures import ThreadPoolExecutor
import time

def work():
    return "Done"

with ThreadPoolExecutor() as executor:
    future = executor.submit(work)
    print(future.result())

# very important concept of map
def square(n):
    time.sleep(1)
    return n*n

with ThreadPoolExecutor() as executor:
    results = executor.map(square,[1,2,3,4,5])
    print(list(results))