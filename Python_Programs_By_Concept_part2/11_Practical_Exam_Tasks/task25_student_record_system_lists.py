# Practical Exam Task 25:
# Develop a menu-driven Student Record Management System using lists that supports:
# - Add student
# - Display all students
# - Search student
# - Update student
# - Delete student
# - Sort by name
# - Sort by marks
# - Display topper
# - Display average marks
# - Exit

# Nested list: [Roll No, Student Name, Marks]
students = [
    [101, "Vrisha Thakkar", 95.0],
    [102, "Aarav Shah", 87.5],
    [103, "Bhavya Patel", 91.0],
    [104, "Diya Mehta", 79.0]
]

def add_student():
    print("\n--- Add New Student ---")
    roll = int(input("Enter Roll Number: "))
    for s in students:
        if s[0] == roll:
            print("Error: Roll Number already exists!")
            return
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))
    students.append([roll, name, marks])
    print(f"Student '{name}' added successfully.")

def display_all():
    print("\n--- All Student Records ---")
    if not students:
        print("No student records found.")
        return
    print(f"{'Roll No':<10}{'Name':<22}{'Marks':<8}")
    print("-" * 40)
    for s in students:
        print(f"{s[0]:<10}{s[1]:<22}{s[2]:<8.2f}")

def search_student():
    print("\n--- Search Student ---")
    roll = int(input("Enter Roll Number to search: "))
    for s in students:
        if s[0] == roll:
            print(f"Found -> Roll No: {s[0]} | Name: {s[1]} | Marks: {s[2]}")
            return
    print("Student not found!")

def update_student():
    print("\n--- Update Student ---")
    roll = int(input("Enter Roll Number to update: "))
    for s in students:
        if s[0] == roll:
            print(f"Current details: Name={s[1]}, Marks={s[2]}")
            s[1] = input("Enter new name: ")
            s[2] = float(input("Enter new marks: "))
            print("Student updated successfully.")
            return
    print("Student not found!")

def delete_student():
    print("\n--- Delete Student ---")
    roll = int(input("Enter Roll Number to delete: "))
    for i in range(len(students)):
        if students[i][0] == roll:
            deleted = students.pop(i)
            print(f"Deleted student: {deleted[1]} (Roll: {deleted[0]})")
            return
    print("Student not found!")

def sort_by_name():
    print("\n--- Students Sorted by Name ---")
    students.sort(key=lambda s: s[1].lower())
    display_all()

def sort_by_marks():
    print("\n--- Students Sorted by Marks (Highest First) ---")
    students.sort(key=lambda s: s[2], reverse=True)
    display_all()

def display_topper():
    print("\n--- Class Topper ---")
    if not students:
        print("No student records available.")
        return
    topper = max(students, key=lambda s: s[2])
    print(f"TOPPER: {topper[1]} (Roll No {topper[0]}) with {topper[2]} marks!")

def display_average():
    print("\n--- Class Average Marks ---")
    if not students:
        print("No student records available.")
        return
    total_marks = sum(s[2] for s in students)
    avg = total_marks / len(students)
    print(f"Total Students : {len(students)}")
    print(f"Class Average  : {avg:.2f} marks")

def main():
    while True:
        print("\n==========================================")
        print("    STUDENT RECORD MANAGEMENT SYSTEM      ")
        print("==========================================")
        print(" 1. Add student")
        print(" 2. Display all students")
        print(" 3. Search student")
        print(" 4. Update student")
        print(" 5. Delete student")
        print(" 6. Sort by name")
        print(" 7. Sort by marks")
        print(" 8. Display topper")
        print(" 9. Display average marks")
        print("10. Exit")
        print("==========================================")

        ch = input("Enter choice (1-10): ")

        if ch == "1":
            add_student()
        elif ch == "2":
            display_all()
        elif ch == "3":
            search_student()
        elif ch == "4":
            update_student()
        elif ch == "5":
            delete_student()
        elif ch == "6":
            sort_by_name()
        elif ch == "7":
            sort_by_marks()
        elif ch == "8":
            display_topper()
        elif ch == "9":
            display_average()
        elif ch == "10":
            print("Exiting Student Record Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 10.")

if __name__ == "__main__":
    main()
