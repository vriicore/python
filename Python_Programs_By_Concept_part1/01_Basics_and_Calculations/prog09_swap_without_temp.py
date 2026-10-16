# Program 1.9: Swap Without Temp
# Take two numbers a and b as input. Display them.
# Swap using Python tuple: a, b = b, a. Display after swap.
# Also try arithmetic swap (a=a+b; b=a-b; a=a-b).

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"Original values: a = {a}, b = {b}")

# Method 1: Using Python tuple unpacking
a, b = b, a
print(f"After tuple swap: a = {a}, b = {b}")

# Method 2: Using arithmetic operations
a = a + b
b = a - b
a = a - b
print(f"After arithmetic swap (back to original): a = {a}, b = {b}")
