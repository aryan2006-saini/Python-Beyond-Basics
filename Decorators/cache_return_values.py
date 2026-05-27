import time

def cache(func):
    cache_values = {}
    def wrapper(*args):
        if args in cache_values:
            return cache_values[args]
        result = func(*args)
        cache_values[args]=result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a+b

s1 = time.time()
r1 = long_running_function(2,3)
e1 = time.time()

s2 = time.time()
r2 = long_running_function(2,3)
e2 = time.time()

print(f"Result r1={r1} takes {e1-s1} time")
print(f"Result r2={r2} takes {e2-s2} time")

# Output:
# Result r1=5 takes 4.000977516174316 time
# Result r2=5 takes 0.0 time
