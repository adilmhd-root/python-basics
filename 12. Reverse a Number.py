num = float(input("Enter a number to reverse: "))
reversed =0
while num>0:
    last = num %10
    num = num // 10
    reversed = (reversed *10) + last

print("Reversed Number is: ",reversed)