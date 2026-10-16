# Program 1.19: Number Reversal & Palindrome
# Take a number as input.
# (a) Reverse it using while loop.
# (b) Check if original == reversed (palindrome number). Display both results.

num = int(input("Enter an integer number: "))

temp = abs(num)
rev = 0

while temp > 0:
    rem = temp % 10
    rev = (rev * 10) + rem
    temp = temp // 10

if num < 0:
    rev = -rev

print("Original number:", num)
print("Reversed number:", rev)

if num == rev:
    print("Result: The number is a Palindrome!")
else:
    print("Result: The number is NOT a Palindrome.")
