# Program: Rounding Floating-Point Numbers with map()
# Take a list of floats and display:
# 1. Rounded to nearest integer
# 2. Rounded to 2 decimal points

floats = [6.56773, 9.57668, 4.00914, 56.24241, 9.01344]

round_int = list(map(lambda x: round(x), floats))
round_two = list(map(lambda x: round(x, 2), floats))

print("Original Floats :", floats)
print("Rounded to Int  :", round_int)
print("Rounded to 2 dec:", round_two)
