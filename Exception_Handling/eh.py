a = int(input("Enter a number: "))
if a<0:
    raise ValueError("I don't divide negative numbers.")
try:
    print(10/int(a))
except Exception as e:
    print(type(e))
    print(e)
finally:
    print("Executed")