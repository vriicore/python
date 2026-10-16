# Program: Common Elements and Difference Between Two Lists
# 1. Common elements (intersection)
# 2. Elements present in list1 but not list2 (difference)

l1 = [1, 2, 3, 4, 5, 6]
l2 = [4, 5, 6, 7, 8, 9]

print("List 1:", l1)
print("List 2:", l2)

# common elements
common = []
for x in l1:
    if x in l2 and x not in common:
        common.append(x)

# elements in list1 but not list2
only_in_l1 = []
for x in l1:
    if x not in l2 and x not in only_in_l1:
        only_in_l1.append(x)

print("Common elements (Intersection):", common)
print("In List 1 but not List 2 (Difference):", only_in_l1)
