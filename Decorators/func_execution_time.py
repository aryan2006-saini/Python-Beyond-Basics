#Write a function which calculate time of execution of any function
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        print(f"function {func.__name__} ran in {end-start} time")
        return value
    return wrapper

@timer  ### this is decorator
def example_function(n):
    time.sleep(n)

example_function(2)

## Output--->  [function example_function ran in 2.004917621612549 time]