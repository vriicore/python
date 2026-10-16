# Program: Employee Dictionary Operations
# 1. Create dictionary of employees where empId is key and name is value.
# 2. Display count of employees.
# 3. Make separate list of IDs and separate list of Names.
# 4. Check if empId exists: if yes display name, if not add ID and Name.
# 5. Update/change employee name.
# 6. Remove employee by ID.

employees = {
    101: "Rahul Sharma",
    102: "Priya Patel",
    103: "Amit Shah",
    104: "Neha Gupta"
}
print("Initial Employees Dictionary:", employees)

# 2. Total count
print("Total Employees:", len(employees))

# 3. Separate lists
id_list = list(employees.keys())
name_list = list(employees.values())
print("Employee IDs List  :", id_list)
print("Employee Names List:", name_list)

# 4. Search and Add
search_id = int(input("\nEnter Employee ID to search/verify: "))
if search_id in employees:
    print(f"Employee Found: {employees[search_id]}")
else:
    new_name = input("Employee not found! Enter name to add: ")
    employees[search_id] = new_name
    print(f"Added new employee: {search_id} -> {new_name}")

# 5. Update name
update_id = 101
if update_id in employees:
    employees[update_id] = "Rahul M. Sharma"
    print(f"Updated ID {update_id} name to: {employees[update_id]}")

# 6. Remove employee
remove_id = 104
if remove_id in employees:
    removed_name = employees.pop(remove_id)
    print(f"Removed ID {remove_id} ({removed_name})")

print("\nFinal Employees Dictionary:", employees)
