# Program 2.10: Report Card with f-strings
# Create variables: student_name, roll_no, marks_5_subjects.
# Calculate total, percentage, grade.
# Display a formatted report card using f-strings with proper alignment.

student_name = "Vrisha Thakkar"
roll_no = "MSCIT-301"
marks = [85, 90, 78, 88, 92]
subjects = ["Python", "Database", "Networking", "Data Structures", "Web Tech"]

total = sum(marks)
percentage = total / len(marks)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("=" * 45)
print(f"{'STUDENT REPORT CARD':^45}")
print("=" * 45)
print(f"Name   : {student_name:<20} Roll No: {roll_no}")
print("-" * 45)
print(f"{'Subject':<25}{'Max Marks':<10}{'Marks Obtained'}")
print("-" * 45)
for sub, mark in zip(subjects, marks):
    print(f"{sub:<25}{100:<10}{mark:<10}")
print("-" * 45)
print(f"Total Marks : {total} / 500")
print(f"Percentage  : {percentage:.2f}%")
print(f"Final Grade : {grade}")
print("=" * 45)
