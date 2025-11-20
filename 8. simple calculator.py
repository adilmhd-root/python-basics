#SIMPLE CALCULATOR

a = float(input("enter a number: "))
b = float(input("enter another number: "))
ab = input("what you want to do (/ * - + )")

if ab=='+':
    print("addition= ",a + b)

if ab=='-':
    print("subtraction= ",a - b)

if ab=='/':
    print("division= ",a / b)

if ab=='*':
    print("multiplication= ",a * b)

if ab=='%':
    print("modulus= ",a % b)


print("thanks !!")