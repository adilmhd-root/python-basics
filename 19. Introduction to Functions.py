#   Introduction to Functions


# 1️⃣ Example: Simple function with no input
def greet():
    print("Welcome to the Function Project!")
    print("This shows how functions work.\n")


# 2️⃣ Example: Function with one input
def say_hello(name):
    print("Hello " + name + "! Nice to meet you.\n")


# 3️⃣ Example: Function with two inputs
def add_numbers(a, b):
    result = a + b
    print("Adding", a, "and", b, "gives:", result, "\n")


# 4️⃣ Example: Function that RETURNS a value
def multiply(x, y):
    return x * y



# -----------------------------
#      Program Starts Here


# calling function 1
greet()


# calling function 2
username = input("Enter your name: ")
say_hello(username)


# calling function 3
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
add_numbers(n1, n2)


# calling function 4
print("Now let's multiply two numbers:")
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

answer = multiply(a, b)     # <- using return value
print("Multiplication result:", answer)
