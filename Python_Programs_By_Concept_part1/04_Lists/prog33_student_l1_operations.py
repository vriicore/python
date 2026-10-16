# Program: Student List L1 Comprehensive Practice
# Perform:
# 1. Count students
# 2. Add one more student
# 3. Sort students
# 4. Check if student present
# 5. Count duplicate names and 1st position
# 6. Remove last student
# 7. Remove particular student
# 8. Remove all duplicate instances of student

L1 = ["Amit", "Bina", "Chetan", "Bina", "Dharmesh", "Esha"]
print("Initial L1:", L1)

# 1. Count
print("Total students:", len(L1))

# 2. Add student
L1.append("Falguni")
print("After adding Falguni:", L1)

# 3. Sort
L1.sort()
print("Sorted students:", L1)

# 4 & 5. Search student & count duplicates
search_name = "Bina"
if search_name in L1:
    print(f"'{search_name}' is found in the list.")
    print(f"Count of '{search_name}': {L1.count(search_name)}")
    print(f"First occurrence index: {L1.index(search_name)}")

# 6. Remove last student
popped_student = L1.pop()
print(f"After removing last student ({popped_student}):", L1)

# 7 & 8. Remove all occurrences of a student name
remove_name = "Bina"
while remove_name in L1:
    L1.remove(remove_name)
print(f"After removing all instances of '{remove_name}':", L1)
