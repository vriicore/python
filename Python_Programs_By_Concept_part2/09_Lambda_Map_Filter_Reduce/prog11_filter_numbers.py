# Program: Filter Numbers
# Filter:
# 1. Even numbers
# 2. Odd numbers
# 3. Numbers > 50
# 4. Numbers < 25
# 5. Divisible by 3 and 5
# 6. Positive numbers
# 7. Remove negative numbers

data = [-15, -4, 0, 10, 15, 20, 24, 30, 45, 60, 75, 80]
print("Dataset:", data)

evens = list(filter(lambda x: x % 2 == 0, data))
odds = list(filter(lambda x: x % 2 != 0, data))
gt_50 = list(filter(lambda x: x > 50, data))
lt_25 = list(filter(lambda x: x < 25, data))
div_3_5 = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, data))
positives = list(filter(lambda x: x > 0, data))
non_negatives = list(filter(lambda x: x >= 0, data))

print("Evens            :", evens)
print("Odds             :", odds)
print("Greater than 50  :", gt_50)
print("Less than 25     :", lt_25)
print("Divisible by 3 & 5:", div_3_5)
print("Positives        :", positives)
print("Non-negatives    :", non_negatives)
