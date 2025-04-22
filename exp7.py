def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def calculator():
    print("Hello!")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Please enter the number of the operation: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter number 1: "))
        num2 = float(input("Enter number 2: "))

        if choice == '1':
            print(f"Answer = {add(num1, num2)}")
        elif choice == '2':
            print(f"Answer = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Answer = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Answer = {divide(num1, num2)}")
    else:
        print("Invalid input. Please select a valid operation.")

# Run the calculator function
calculator()
                