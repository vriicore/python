# Program 3.9: Student Gradebook
# Create dictionary: {student_name: [mark1, mark2, mark3]}
# Calculate average for each student.
# Display sorted by average (highest first). Identify top student.

gradebook = {
    "Amit": [85, 90, 88],
    "Bhavya": [92, 94, 96],
    "Chetan": [70, 75, 72],
    "Diya": [88, 85, 90],
    "Eshan": [60, 65, 70]
}

student_averages = {}
for student, marks in gradebook.items():
    student_averages[student] = sum(marks) / len(marks)

# sort by average descending
sorted_students = sorted(student_averages.items(), key=lambda x: x[1], reverse=True)

print("--- STUDENT GRADEBOOK (Sorted by Average) ---")
print(f"{'Student':<15}{'Average Marks'}")
print("-" * 30)
for student, avg in sorted_students:
    print(f"{student:<15}{avg:.2f}")

top_student = sorted_students[0]
print(f"\nTop Student: {top_student[0]} with Average {top_student[1]:.2f}")
