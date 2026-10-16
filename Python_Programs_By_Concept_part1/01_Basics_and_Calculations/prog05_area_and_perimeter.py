# Program 1.5: Area & Perimeter
# Take length and breadth of a rectangle as input.
# Calculate: Area = l*b, Perimeter = 2*(l+b).
# Also calculate area of a circle with radius = length.

pi = 3.14159

l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))

rect_area = l * b
rect_perimeter = 2 * (l + b)

# circle with radius equal to length
circle_area = pi * (l ** 2)

print("Rectangle Area:", rect_area)
print("Rectangle Perimeter:", rect_perimeter)
print("Circle Area (with radius = length):", circle_area)
