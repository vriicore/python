# Program: Min and Max From Tuple Without min() and max()
# Find the maximum and minimum numbers from a tuple without using min() and max().

tup = (45, 12, 89, 23, 7, 65, 98, 3)
print("Tuple values:", tup)

min_val = tup[0]
max_val = tup[0]

for val in tup:
    if val > max_val:
        max_val = val
    if val < min_val:
        min_val = val

print("Maximum value in tuple:", max_val)
print("Minimum value in tuple:", min_val)
