# Program: Remove Duplicates Using filter()
# Remove duplicate numbers from list using list.count() or lambda with seen set.

nums = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]

# Using filter with seen tracking
seen = set()
def is_first_occurrence(x):
    if x in seen:
        return False
    seen.add(x)
    return True

unique_nums = list(filter(is_first_occurrence, nums))

print("Original list :", nums)
print("Unique list   :", unique_nums)
