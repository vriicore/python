# Program 2.4: Multi-Return Function
# Write a function stats(a, b, c) that returns: sum, average, minimum, and maximum of three numbers.
# Unpack and display all 4 results.

def stats(a, b, c):
    s = a + b + c
    avg = s / 3
    mn = min(a, b, c)
    mx = max(a, b, c)
    return s, avg, mn, mx

# Calling function and unpacking
n1, n2, n3 = 45, 12, 88
total, average, minimum, maximum = stats(n1, n2, n3)

print(f"Input Numbers: {n1}, {n2}, {n3}")
print("--- Unpacked Stats ---")
print("Sum     :", total)
print("Average :", round(average, 2))
print("Minimum :", minimum)
print("Maximum :", maximum)
