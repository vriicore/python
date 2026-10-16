# Practical Exam Task 6:
# Create a list of employee names.
# Search for a name, update it if found, otherwise add it to the list.

employees = ["Vrisha Thakkar", "Aarav Shah", "Bhavya Patel", "Chetan Sharma"]
print("Current Employee List:", employees)

search_name = input("\nEnter employee name to search: ")

found = False
for i in range(len(employees)):
    if employees[i].lower() == search_name.lower():
        found = True
        print(f"Employee '{employees[i]}' found at index {i}.")
        new_name = input("Enter new updated name: ")
        employees[i] = new_name
        print("Employee name updated successfully.")
        break

if not found:
    print(f"Employee '{search_name}' not found. Adding to employee list...")
    employees.append(search_name)
    print("Employee added successfully.")

print("\nUpdated Employee List:", employees)
