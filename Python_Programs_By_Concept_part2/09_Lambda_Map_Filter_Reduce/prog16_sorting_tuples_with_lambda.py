# Program: Sort Tuples Using Lambda
# 1. Fruits by price: [(120,'Apple'), (20,'Banana'),(50,'Chikoo'),(100,'Pinaple')]
# 2. Students by marks: [('English', 88), ('Science', 90), ('Maths', 97), ('Social', 82)]
# 3. Employees by salary: [('Amit', 45000), ('Bhavya', 65000), ('Chirag', 52000)]
# 4. Names by length

fruits = [(120, 'Apple'), (20, 'Banana'), (50, 'Chikoo'), (100, 'Pinaple')]
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social', 82)]
employees = [('Amit', 45000), ('Bhavya', 65000), ('Chirag', 52000)]
names = ["Vrisha", "Aarav", "Dharmesh", "Om", "Priya"]

# 1. Sort fruits by price
sorted_fruits = sorted(fruits, key=lambda x: x[0])

# 2. Sort subjects by marks
sorted_subjects = sorted(subject_marks, key=lambda x: x[1])

# 3. Sort employees by salary descending
sorted_employees = sorted(employees, key=lambda x: x[1], reverse=True)

# 4. Sort names by length
sorted_names = sorted(names, key=lambda x: len(x))

print("Sorted Fruits (Price)   :", sorted_fruits)
print("Sorted Subjects (Marks) :", sorted_subjects)
print("Sorted Employees (Salary):", sorted_employees)
print("Sorted Names by Length  :", sorted_names)
