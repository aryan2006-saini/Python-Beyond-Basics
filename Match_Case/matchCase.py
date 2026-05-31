n = input("Enter a number:")
print("1. To print the same number.")
print("2. To print the number by adding  1 to it.")
choice = input("Enter your choice: ")

try:
    match choice:
        case '1':
            print(int(n))
        case '2':
            print(int(n)+1)
        case _:
            print("Invalid Choice")
except ValueError:
    print("Please enter a valid Integer.")

