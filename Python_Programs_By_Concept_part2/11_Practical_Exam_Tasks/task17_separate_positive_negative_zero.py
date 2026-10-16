# Practical Exam Task 17:
# Accept a list of numbers and separate them into positive, negative, and zero lists.

numbers = [12, -7, 0, 45, -3, 0, 89, -15, 0, 24, -8]
print("All Numbers:", numbers)

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

print("\n--- Separated Lists ---")
print("Positive Numbers :", positives)
print("Negative Numbers :", negatives)
print("Zero Elements    :", zeros)
