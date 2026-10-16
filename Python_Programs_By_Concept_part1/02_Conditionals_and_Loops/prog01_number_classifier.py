# Program 1.13: Number Classifier
# Take a number as input. Check and display:
# (a) positive/negative/zero
# (b) even or odd
# (c) divisible by 5 or not

num = int(input("Enter an integer number: "))

# (a) Check positive, negative or zero
if num > 0:
    sign = "Positive"
elif num < 0:
    sign = "Negative"
else:
    sign = "Zero"

# (b) Check even or odd
if num % 2 == 0:
    parity = "Even"
else:
    parity = "Odd"

# (c) Check divisibility by 5
if num % 5 == 0:
    div5 = "Divisible by 5"
else:
    div5 = "Not divisible by 5"

print("Results:")
print(f"1. The number is {sign}")
print(f"2. The number is {parity}")
print(f"3. The number is {div5}")
