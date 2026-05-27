## write a program to create a decorator print the function name and the values of arguments everytime the function is called:

def debug(func):
    def wrapper(*args, **kwargs):
        arg_values = ','.join(str(arg) for arg in args)
        kwargs_values = ','.join(f"{k}={v}" for k,v in kwargs.items())

        print(f"Calling {func.__name__} with args:{arg_values} and kwargs:{kwargs_values}")

        return func(*args, **kwargs)
    
    return wrapper

@debug
def hello():
    print("Hello!")

@debug
def greet(name, greeting="Hello!"):
    print(f"{greeting}, {name}")


hello()
greet("Alice",greeting="Hi")

#output: 
# Calling hello with args: and kwargs:
# Hello!
# Calling greet with args:Alice and kwargs:greeting=Hi
# Hi, Alice