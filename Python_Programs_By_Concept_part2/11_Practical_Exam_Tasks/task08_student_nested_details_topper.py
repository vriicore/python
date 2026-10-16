# Practical Exam Task 8:
# Create a nested list containing student details (Roll No., Name, Marks).
# Display topper details and sort students according to marks.

students = [
    [101, "Aarav Shah", 85.5],
    [102, "Vrisha Thakkar", 96.0],
    [103, "Bhavya Patel", 91.0],
    [104, "Chetan Mehta", 78.0],
    [105, "Diya Mehta", 88.5]
]

print("--- ALL STUDENT DETAILS ---")
print(f"{'Roll No':<10}{'Name':<20}{'Marks'}")
print("-" * 40)
for s in students:
    print(f"{s[0]:<10}{s[1]:<20}{s[2]}")

# Display topper details
topper = max(students, key=lambda s: s[2])
print(f"\nTOPPER: Roll No: {topper[0]} | Name: {topper[1]} | Marks: {topper[2]}")

# Sort students according to marks (descending)
sorted_students = sorted(students, key=lambda s: s[2], reverse=True)
print("\n--- STUDENTS SORTED ACCORDING TO MARKS (Highest First) ---")
print(f"{'Rank':<8}{'Roll No':<10}{'Name':<20}{'Marks'}")
print("-" * 48)
for rank, s in enumerate(sorted_students, 1):
    print(f"{rank:<8}{s[0]:<10}{s[1]:<20}{s[2]}")
