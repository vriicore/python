# Program: Menu-driven Mathematical Operations
# Perform addition, subtraction, multiplication, division, integer division, power.
# Always return values from the functions.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error: Div by Zero"

def integer_division(x, y):
    return x // y if y != 0 else "Error: Div by Zero"

def power(x, y):
    return x ** y

# Sample execution
print("1. Addition (15 + 4)        =", add(15, 4))
print("2. Subtraction (15 - 4)     =", subtract(15, 4))
print("3. Multiplication (15 * 4)  =", multiply(15, 4))
print("4. Float Division (15 / 4)  =", divide(15, 4))
print("5. Integer Division (15 // 4)=", integer_division(15, 4))
print("6. Power (15 ** 4)          =", power(15, 4))
