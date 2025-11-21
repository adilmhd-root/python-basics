print("enter a word:")
wrd = input(": ")
vowels = 'aeiouAEIOU'
count = 0
for letter in wrd:
    if letter in vowels:
        count = (count + 1)
print("Number of vowels in the word is:", count)