# Program: Search in Nested Personal Profile Tuple
# Create a nested tuple t4: (name, (hobbies), (friends), degree).
# Search for an element and print its position if found, otherwise 'Not found'.

t4 = (
    "Vrisha Thakkar",
    ("Coding", "Cricket", "Music"),
    ("Aarav", "Bhavya", "Chirag"),
    "M.Sc. IT"
)

print("Profile Nested Tuple (t4):")
print(t4)

search_term = input("\nEnter element to search: ")

found = False
for i, item in enumerate(t4):
    if item == search_term:
        print(f"Found '{search_term}' at top-level index [{i}].")
        found = True
        break
    elif isinstance(item, tuple):
        for j, sub_item in enumerate(item):
            if sub_item.lower() == search_term.lower():
                print(f"Found '{search_term}' at nested index [{i}][{j}] inside {item}.")
                found = True
                break
    if found:
        break

if not found:
    print(f"'{search_term}' is Not found in the tuple.")
