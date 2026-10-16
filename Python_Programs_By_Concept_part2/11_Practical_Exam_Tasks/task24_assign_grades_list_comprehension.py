# Practical Exam Task 24:
# Accept a list of marks and assign grades (A, B, C, D, F) using list comprehension.

marks_list = [95, 82, 74, 63, 48, 89, 91, 55, 32, 78]
print("Student Marks:", marks_list)

# Grading criteria:
# >= 90 : A
# >= 80 : B
# >= 70 : C
# >= 50 : D
# < 50  : F

grades = [
    'A' if m >= 90 else
    'B' if m >= 80 else
    'C' if m >= 70 else
    'D' if m >= 50 else
    'F'
    for m in marks_list
]

print("\n--- Marks and Assigned Grades ---")
print(f"{'Marks':<10}{'Grade'}")
print("-" * 20)
for m, g in zip(marks_list, grades):
    print(f"{m:<10}{g}")
