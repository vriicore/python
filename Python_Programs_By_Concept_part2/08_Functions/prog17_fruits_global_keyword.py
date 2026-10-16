# Program: Global Keyword with Fruits List
# Create a list of fruits and perform operations using separate functions:
# Show use of global keyword and globals(), do not return from functions.
# 1. Add fruit at last
# 2. Insert fruit at particular position (default pos = 1)
# 3. Update fruit using keyword arguments
# 4. Remove fruit (by index or name)
# 5. Arrange fruits in order

fruits = ["Apple", "Banana", "Cherry"]

def add_last(new_fruit):
    global fruits
    fruits.append(new_fruit)
    print(f"Added at last: {new_fruit}")

def insert_fruit(new_fruit, pos=1):
    global fruits
    fruits.insert(pos, new_fruit)
    print(f"Inserted '{new_fruit}' at position {pos}")

def update_fruit(*, old_name, new_name):
    global fruits
    if old_name in fruits:
        idx = fruits.index(old_name)
        fruits[idx] = new_name
        print(f"Updated '{old_name}' to '{new_name}'")
    else:
        print(f"'{old_name}' not found for update.")

def remove_fruit(identifier):
    global fruits
    # check if integer index or string name
    if isinstance(identifier, int):
        if 0 <= identifier < len(fruits):
            removed = fruits.pop(identifier)
            print(f"Removed item '{removed}' at index {identifier}")
    elif identifier in fruits:
        fruits.remove(identifier)
        print(f"Removed '{identifier}' by name")
    else:
        print(f"Item {identifier} not found!")

def arrange_fruits():
    # using globals() dictionary demonstration
    global_dict = globals()
    global_dict['fruits'].sort()
    print("Arranged fruits in alphabetical order.")

# Demonstration
print("Initial fruits:", fruits)
add_last("Mango")
insert_fruit("Grapes")  # pos defaults to 1
update_fruit(old_name="Banana", new_name="Blueberry")
remove_fruit("Cherry")
arrange_fruits()
print("Final fruits list:", fruits)
