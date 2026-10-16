# Program: Find All Pairs that Sum to Target Value
# Given a list and a target sum, find all unique pairs that equal target.

numbers = [2, 4, 3, 5, 7, 8, 9, -1, 6]
target = 7
print("Numbers list:", numbers)
print("Target sum  :", target)

pairs = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))

print("Pairs that sum to target:", pairs)
