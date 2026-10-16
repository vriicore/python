# Program: Conditional Map on Two Lists
# Take 2 lists and add elements if 1st > 2nd, else find difference.
# nums1 = [6, 5, 3, 9], nums2 = [0, 1, 7, 7] -> O/P: [6, 4, 4, 2] (or 7-3=4)

nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]

result = list(map(lambda a, b: a + b if a > b else abs(a - b), nums1, nums2))

print("Nums 1 :", nums1)
print("Nums 2 :", nums2)
print("Output :", result)
