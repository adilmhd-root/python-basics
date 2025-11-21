#Take three inputs → print which one is the largest number
num1 = float(input("enter number 1: "))
num2 = float(input("wnter number 2: "))
num3 = float(input("enter number 3: "))

if num1>num2>num3:
    print("number 1 is the largest")
elif num2>num1 and num2>num3:
    print("number 2 is the largest")
elif num3>num1 and num3>num2:
    print("number 3 is the largest")
elif num1==num2==num3:
    print("all numbers are equal")
else:
    print("two numbers are equal and largest")


