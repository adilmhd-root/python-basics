data = input("enter numbers separated by space: ")
nums = list(map(int, data.split()))

largest = max(nums)
second_largest = None

for n in nums:
    if n != largest:
        if second_largest is None or n > second_largest:
            second_largest = n

print("second largest number:", second_largest)