# Program: Menu-driven City CRUD Operations
# Supports:
# 1. Create (Add new city)
# 2. Read (Display all cities)
# 3. Update (Modify existing city)
# 4. Delete (Remove a city)
# 5. Search city
# 6. Exit

cities = ["Ahmedabad", "Surat", "Vadodara", "Rajkot"]

def display_cities():
    print("\n--- List of Cities ---")
    if not cities:
        print("No cities stored.")
    else:
        for i, city in enumerate(cities, 1):
            print(f"{i}. {city}")

def add_city():
    city = input("Enter city name: ")
    if city in cities:
        print("City already in list.")
    else:
        cities.append(city)
        print(f"'{city}' added successfully.")

def update_city():
    old = input("Enter existing city to update: ")
    if old in cities:
        new_city = input("Enter updated city name: ")
        idx = cities.index(old)
        cities[idx] = new_city
        print("City updated.")
    else:
        print("City not found!")

def delete_city():
    city = input("Enter city name to delete: ")
    if city in cities:
        cities.remove(city)
        print(f"'{city}' deleted.")
    else:
        print("City not found!")

def search_city():
    city = input("Enter city to search: ")
    if city in cities:
        print(f"Found: '{city}' is at index {cities.index(city)}.")
    else:
        print("City not found.")

def main():
    while True:
        print("\n--- CITIES CRUD MENU ---")
        print("1. Display All Cities")
        print("2. Add City")
        print("3. Update City")
        print("4. Delete City")
        print("5. Search City")
        print("6. Exit")

        ch = input("Enter choice (1-6): ")
        if ch == "1":
            display_cities()
        elif ch == "2":
            add_city()
        elif ch == "3":
            update_city()
        elif ch == "4":
            delete_city()
        elif ch == "5":
            search_city()
        elif ch == "6":
            print("Exiting Cities CRUD.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    display_cities()
    # main()
