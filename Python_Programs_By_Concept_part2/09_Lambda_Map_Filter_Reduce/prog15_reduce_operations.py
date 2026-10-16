# Program: Reduce Operations
# 1. Sum of all elements
# 2. Product of all elements
# 3. Maximum element from list

from functools import reduce

nums = [3, 7, 2, 9, 5, 8]

sum_all = reduce(lambda a, b: a + b, nums)
prod_all = reduce(lambda a, b: a * b, nums)
max_elem = reduce(lambda a, b: a if a > b else b, nums)

print("Numbers list:", nums)
print("Sum of elements     :", sum_all)
print("Product of elements :", prod_all)
print("Maximum element     :", max_elem)
