# Program: Substring Search & Occurrences
# Take two strings s1 and s2:
# 1. Check whether s2 is present in s1
# 2. Print 1st and last occurrence positions
# 3. Count total number of times s2 occurs in s1

s1 = input("Enter main string (s1): ")
s2 = input("Enter substring to search (s2): ")

if s2 in s1:
    print(f"'{s2}' is present in '{s1}'.")
    first_pos = s1.find(s2)
    last_pos = s1.rfind(s2)
    count = s1.count(s2)

    print("First occurrence index:", first_pos)
    print("Last occurrence index :", last_pos)
    print("Total occurrences     :", count)
else:
    print(f"'{s2}' was not found in '{s1}'.")
