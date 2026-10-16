# Program 2.7: Modular Calculator Functions
# Write 5 functions: add(a, b), subtract(a, b), multiply(a, b), divide(a, b), power(a, b).
# Handle ZeroDivisionError in divide(). Menu-driven.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

def power(a, b):
    return a ** b

# Demonstration of calculator
print("--- Calculator Test ---")
x, y = 10, 2
print(f"Numbers: x={x}, y={y}")
print("Add     :", add(x, y))
print("Subtract:", subtract(x, y))
print("Multiply:", multiply(x, y))
try:
    print("Divide  :", divide(x, y))
    print("Divide by 0 test:")
    divide(x, 0)
except ZeroDivisionError as err:
    print("Caught Error:", err)

print("Power   :", power(x, y))
