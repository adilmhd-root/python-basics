# Simple Calculator Project


# Function to add two numbers
def add(a, b):
    return a + b


# Function to subtract two numbers
def sub(a, b):
    return a - b


# Function to multiply two numbers
def mul(a, b):
    return a * b


# Function to divide safely
def div(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


# Main function – handles user input and shows output
def calculator():

    print("---- Simple Calculator ----")

    # input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Select (1/2/3/4): ")

    print("\nResult:")

    if choice == "1":
        print(add(num1, num2))

    elif choice == "2":
        print(sub(num1, num2))

    elif choice == "3":
        print(mul(num1, num2))

    elif choice == "4":
        print(div(num1, num2))

    else:
        print("Invalid option!")


# run the project
calculator()

