# Program: Find Missing Numbers in Range
# Accept a list of integers and find all missing numbers between minimum and maximum value.

nums = [10, 12, 15, 17, 20]
print("Input list:", nums)

min_val = min(nums)
max_val = max(nums)
print(f"Range is from {min_val} to {max_val}")

missing = []
for x in range(min_val, max_val + 1):
    if x not in nums:
        missing.append(x)

print("Missing numbers:", missing)
