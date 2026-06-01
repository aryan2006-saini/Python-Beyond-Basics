class Myerror(Exception):
    def __init__(self, num):
        super().__init__(f"{num} is less than 0. Must be +ve.")

a = int(input("Enter a number: "))
if a<0:
    raise Myerror(a)
try:
    print(10/int(a))
except Exception as e:
    print(type(e))
    print(e)
finally:
    print("Executed")