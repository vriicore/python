# Program: Handle Negative Numbers & Separate Positive, Negative, Zero
# 1. Replace every negative number with zero.
# 2. Separate into positive, negative, and zero lists.

numbers = [12, -7, 0, 45, -3, 0, 89, -15, 24]
print("Original numbers:", numbers)

# 1. Replace negative with 0
replaced = []
for n in numbers:
    if n < 0:
        replaced.append(0)
    else:
        replaced.append(n)

print("After replacing negatives with zero:", replaced)

# 2. Separate into 3 lists
positives = []
negatives = []
zeros = []

for n in numbers:
    if n > 0:
        positives.append(n)
    elif n < 0:
        negatives.append(n)
    else:
        zeros.append(n)

print("Positive numbers :", positives)
print("Negative numbers :", negatives)
print("Zeros            :", zeros)
