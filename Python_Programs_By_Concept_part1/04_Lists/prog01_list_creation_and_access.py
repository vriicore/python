# Program: List Creation & Basic Access
# Write a program to:
# 1. Create a list of 10 numbers and print it.
# 2. Find the length of a list.
# 3. Access first, last, and middle elements.

# creating list of 10 numbers
nums = [12, 45, 7, 23, 89, 56, 34, 91, 18, 62]
print("Original List:", nums)

# length of list
print("Length of list:", len(nums))

# accessing elements
first = nums[0]
last = nums[-1]
mid_idx = len(nums) // 2
middle = nums[mid_idx]

print("First element :", first)
print("Middle element:", middle)
print("Last element  :", last)
