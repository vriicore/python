# Program: Subject-wise Min and Max Marks
# 5 students' marks in 6 subjects (out of 50).
# Calculate and display minimum and maximum marks for each subject in a dictionary.

# Marks matrix: 5 students x 6 subjects
subject_names = ["Maths", "Python", "DS", "DBMS", "OS", "Networking"]
student_records = {
    1: [45, 48, 38, 42, 40, 44],
    2: [35, 42, 40, 39, 45, 38],
    3: [50, 49, 46, 48, 47, 49],
    4: [28, 32, 30, 35, 34, 30],
    5: [42, 40, 44, 41, 43, 45]
}

subject_stats = {}
for sub_idx, sub_name in enumerate(subject_names):
    marks_in_sub = [student_records[roll][sub_idx] for roll in student_records]
    subject_stats[sub_name] = {
        "Min": min(marks_in_sub),
        "Max": max(marks_in_sub)
    }

print("--- SUBJECT-WISE MINIMUM & MAXIMUM MARKS ---")
print(f"{'Subject':<15}{'Min Marks':<15}{'Max Marks'}")
print("-" * 40)
for sub, stats in subject_stats.items():
    print(f"{sub:<15}{stats['Min']:<15}{stats['Max']}")
