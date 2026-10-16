# Program: Student Details with Initials as Key & Youngest Student
# Take 5 student names, store in dict where key is initial and value is [age, degree, fav subject].
# Find and display the youngest student.

students = {
    "A": [21, "B.Sc. IT", "Python"],
    "B": [19, "BCA", "Database"],
    "C": [23, "MCA", "Cloud Computing"],
    "D": [20, "M.Sc. IT", "Machine Learning"],
    "E": [22, "B.Tech", "Web Development"]
}

print("Student Records:")
for initial, details in students.items():
    print(f"Initial: {initial} | Age: {details[0]}, Degree: {details[1]}, Fav Subject: {details[2]}")

# Find youngest student (minimum age)
youngest_initial = min(students, key=lambda k: students[k][0])
youngest_details = students[youngest_initial]

print(f"\nYoungest Student: Initial '{youngest_initial}' with Age {youngest_details[0]} ({youngest_details[1]})")
