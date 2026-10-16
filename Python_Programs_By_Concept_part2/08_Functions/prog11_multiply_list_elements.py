# Program: Multiply All Numbers in a List
# Write a Python function to multiply all the numbers in a list.

def multiply_list(numbers):
    if not numbers:
        return 0
    product = 1
    for num in numbers:
        product *= num
    return product

nums = [2, 3, 4, 5]
result = multiply_list(nums)
print(f"Numbers: {nums}")
print(f"Product of all numbers = {result}")
