# Program: Fruit Tuple Search
# Create a tuple of 5 fruits.
# Ask user to input a fruit name and search in the fruit tuple with suitable message.

fruits = ("Apple", "Banana", "Mango", "Orange", "Pineapple")
print("Available Fruits Tuple:", fruits)

search_fruit = input("Enter fruit name to search: ")

# case-insensitive search
found = False
for f in fruits:
    if f.lower() == search_fruit.lower():
        found = True
        break

if found:
    print(f"Success: '{search_fruit}' is available in the fruits tuple!")
else:
    print(f"Sorry: '{search_fruit}' is not present in the fruits tuple.")
