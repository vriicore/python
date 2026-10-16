# Practical Exam Task 18:
# Create a list of cities.
# Perform all CRUD (Create, Read, Update, Delete) operations using a menu-driven approach.

cities = ["Ahmedabad", "Surat", "Vadodara", "Rajkot"]

def display_cities():
    print("\n--- List of Cities (Read) ---")
    if not cities:
        print("No cities stored in the list.")
    else:
        for idx, city in enumerate(cities, 1):
            print(f"{idx}. {city}")

def add_city():
    city = input("Enter city name to add (Create): ")
    if city in cities:
        print("City already exists in list.")
    else:
        cities.append(city)
        print(f"'{city}' added successfully.")

def update_city():
    old_city = input("Enter city name to update: ")
    if old_city in cities:
        new_city = input("Enter new city name: ")
        idx = cities.index(old_city)
        cities[idx] = new_city
        print(f"City '{old_city}' updated to '{new_city}'.")
    else:
        print("City not found!")

def delete_city():
    city = input("Enter city name to delete: ")
    if city in cities:
        cities.remove(city)
        print(f"City '{city}' deleted successfully.")
    else:
        print("City not found!")

def main():
    while True:
        print("\n===== CITIES CRUD MENU =====")
        print("1. Display All Cities (Read)")
        print("2. Add City (Create)")
        print("3. Update City (Update)")
        print("4. Delete City (Delete)")
        print("5. Exit")
        print("============================")

        ch = input("Enter choice (1-5): ")
        if ch == "1":
            display_cities()
        elif ch == "2":
            add_city()
        elif ch == "3":
            update_city()
        elif ch == "4":
            delete_city()
        elif ch == "5":
            print("Exiting Cities CRUD system. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
