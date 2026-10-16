# Program: Check Number in Specified Range
# Write a UDF to check whether an inputted number is between specified range or not.

def check_in_range(num, low, high):
    if low <= num <= high:
        return True
    return False

# Test
n = 35
lower_bound, upper_bound = 10, 50

if check_in_range(n, lower_bound, upper_bound):
    print(f"{n} is inside the range [{lower_bound}, {upper_bound}].")
else:
    print(f"{n} is outside the range [{lower_bound}, {upper_bound}].")
