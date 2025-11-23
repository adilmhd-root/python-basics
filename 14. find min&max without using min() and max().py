data = input("enter numbers (separated by space): ")

nums = list(map(int, data.split()))

small = nums[0]
big = nums[0]

for n in nums:
    if n < small:
        small = n
    if n > big:
        big = n

print("min:", small)
print("max:", big)
