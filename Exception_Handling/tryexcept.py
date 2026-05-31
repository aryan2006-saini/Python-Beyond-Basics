a = input("Enter a number: ")

try:
    print(f"table of {a}:" )
    for i in range(1,11):
        print(f"{a} X {i} = ",int(a)*i)

except ValueError:
    print("Enter a valid number.")