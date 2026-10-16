# Program: Area Functions
# Create functions to calculate:
# 1. Area of rectangle = width * length
# 2. Area of triangle  = 0.5 * height * base
# 3. Area of circle    = pi * r * r

import math

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return math.pi * (radius ** 2)

print("Area of Rectangle (l=10, w=5) :", area_rectangle(10, 5))
print("Area of Triangle (b=8, h=6)   :", area_triangle(8, 6))
print("Area of Circle (r=7)          :", round(area_circle(7), 2))
