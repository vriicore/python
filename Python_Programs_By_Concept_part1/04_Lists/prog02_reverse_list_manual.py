# Program: Reverse a List Without reverse()
# Reverse a list without using the built-in reverse() method.

nums = [10, 20, 30, 40, 50]
print("Original list:", nums)

# Method 1: Using slicing
rev_slice = nums[::-1]
print("Reversed using slicing:", rev_slice)

# Method 2: Using manual loop (student approach)
rev_manual = []
for i in range(len(nums) - 1, -1, -1):
    rev_manual.append(nums[i])
print("Reversed using manual loop:", rev_manual)
