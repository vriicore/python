# Program: Student Results & Topper from Dictionary
# 1. Dictionary: {rollno: [marks in 5 subjects]}
# 2. Compute: {rollno: (total, percentage, grade)}
# 3. Find roll number who scored highest total marks (topper).

marks_data = {
    101: [78, 85, 90, 72, 88],
    102: [92, 95, 89, 94, 90],
    103: [65, 70, 60, 58, 62],
    104: [80, 82, 84, 79, 85]
}

results = {}
for roll, marks in marks_data.items():
    tot = sum(marks)
    pct = tot / 5
    if pct >= 80:
        grd = "A"
    elif pct >= 60:
        grd = "B"
    elif pct >= 40:
        grd = "C"
    else:
        grd = "Fail"
    results[roll] = (tot, pct, grd)

print("--- STUDENT RESULTS (Total, Percentage, Grade) ---")
print(f"{'Roll No':<10}{'Total':<10}{'Percentage':<15}{'Grade'}")
print("-" * 45)
for roll, res in results.items():
    print(f"{roll:<10}{res[0]:<10}{res[1]:<15.2f}{res[2]}")

# Find topper
topper_roll = max(results, key=lambda r: results[r][0])
print(f"\nTopper is Roll No {topper_roll} with Total {results[topper_roll][0]} ({results[topper_roll][1]}%)")
