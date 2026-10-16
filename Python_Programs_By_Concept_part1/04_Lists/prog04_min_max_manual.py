# Program: Maximum and Minimum Without max()/min()
# Write a program to find maximum and minimum without using max() and min().

nums = [45, 12, 89, 23, 5, 67, 99, 34]
print("Numbers list:", nums)

# assume first element is both min and max
min_val = nums[0]
max_val = nums[0]

for x in nums:
    if x > max_val:
        max_val = x
    if x < min_val:
        min_val = x

print("Maximum value:", max_val)
print("Minimum value:", min_val)
