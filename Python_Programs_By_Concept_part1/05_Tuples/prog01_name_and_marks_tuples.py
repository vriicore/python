# Program: Name and Marks Tuples (Nested Tuple)
# 1. Create a tuple for name t1 (FirstName, MiddleName, LastName)
# 2. Create a tuple t2 for marks of 5 subjects
# 3. Make total of all marks (with and without sum())
# 4. Make a nested tuple t3 = (t1, t2)
# 5. Search whether an input number is present in t3

# 1. Name tuple
t1 = ("Vrisha", "B", "Thakkar")
print("Name Tuple (t1):", t1)

# 2. Marks tuple
t2 = (85, 90, 78, 88, 92)
print("Marks Tuple (t2):", t2)

# 3. Total marks
# with sum()
total_with_sum = sum(t2)
# without sum()
total_manual = 0
for m in t2:
    total_manual += m

print("Total Marks (with sum())   :", total_with_sum)
print("Total Marks (without sum()):", total_manual)

# 4. Nested tuple
t3 = (t1, t2)
print("Nested Tuple (t3):", t3)

# 5. Search number in t3
num_to_search = int(input("\nEnter a number to search in nested tuple: "))
found = False
for item in t3:
    if isinstance(item, tuple) and num_to_search in item:
        found = True
        break

if found:
    print(f"{num_to_search} is found inside the nested tuple t3!")
else:
    print(f"{num_to_search} is NOT present in the nested tuple t3.")
