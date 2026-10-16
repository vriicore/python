# Program: Nested List for Students & Topper Details
# Nested list: [Roll No., Name, Marks]
# Display topper details and sort students according to marks.

students = [
    [101, "Aarav", 85],
    [102, "Bhavya", 94],
    [103, "Chirag", 78],
    [104, "Diya", 91],
    [105, "Eshan", 88]
]

print("--- All Student Details ---")
print(f"{'Roll No':<10}{'Name':<15}{'Marks'}")
print("-" * 35)
for s in students:
    print(f"{s[0]:<10}{s[1]:<15}{s[2]}")

# Find topper
topper = max(students, key=lambda x: x[2])
print(f"\nTOPPER: Roll {topper[0]} - {topper[1]} with {topper[2]} marks!")

# Sort by marks descending
sorted_by_marks = sorted(students, key=lambda x: x[2], reverse=True)
print("\n--- Students Sorted by Marks (High to Low) ---")
for s in sorted_by_marks:
    print(f"{s[1]:<15} : {s[2]} marks")
