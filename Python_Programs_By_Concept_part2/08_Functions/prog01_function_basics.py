# Program 2.1: Function Basics
# Write 3 functions:
# (a) greet(name) - prints greeting
# (b) square(n) - returns n^2
# (c) cube(n) - returns n^3
# Call each function 3 times with different values.

def greet(name):
    print(f"Hello, {name}! Welcome to Python Lab.")

def square(n):
    return n * n

def cube(n):
    return n * n * n

# Calling greet 3 times
greet("Vrisha")
greet("Aarav")
greet("Pooja")

# Calling square 3 times
print("\nSquares:")
print("Square of 4  :", square(4))
print("Square of 7  :", square(7))
print("Square of 12 :", square(12))

# Calling cube 3 times
print("\nCubes:")
print("Cube of 2 :", cube(2))
print("Cube of 5 :", cube(5))
print("Cube of 9 :", cube(9))
