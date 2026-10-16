# Program 3.10: Duplicate Remover & Set Operations
# Take N numbers in a list:
# (a) Remove duplicates using set.
# (b) Find elements present in list 1 but not list 2 using set difference.
# (c) Count how many times each unique number appears.

list1 = [10, 20, 20, 30, 40, 40, 50, 10]
list2 = [30, 40, 60, 70]

print("List 1:", list1)
print("List 2:", list2)

# (a) Remove duplicates using set
unique_set = set(list1)
print("\n(a) Unique elements using set:", sorted(unique_set))

# (b) Elements in list1 but not in list2
diff_set = set(list1) - set(list2)
print("(b) Elements in List 1 but not List 2:", sorted(diff_set))

# (c) Frequency count using unique set
print("\n(c) Frequency of each number:")
for num in sorted(unique_set):
    print(f"Number {num} appears {list1.count(num)} times.")
