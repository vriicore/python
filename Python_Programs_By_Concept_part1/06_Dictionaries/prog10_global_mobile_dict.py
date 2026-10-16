# Program: Global Mobile Dictionary System
# Create a dictionary for storing price and features of mobile phones.
# Define dictionary as a global variable.
# Use separate functions to add, update, and delete elements.

mobiles = {}

def create():
    global mobiles
    mobiles = {
        "iPhone 15": {"price": 79900, "ram": "6GB", "storage": "128GB"},
        "Samsung S24": {"price": 74999, "ram": "8GB", "storage": "256GB"}
    }
    print("Mobile dictionary initialized globally.")

def add_mobile(model, price, ram, storage):
    global mobiles
    mobiles[model] = {"price": price, "ram": ram, "storage": storage}
    print(f"Added mobile: {model}")

def update_mobile(model, new_price):
    global mobiles
    if model in mobiles:
        mobiles[model]["price"] = new_price
        print(f"Updated price for {model} to Rs. {new_price}")
    else:
        print(f"Model {model} not found!")

def delete_mobile(model):
    global mobiles
    if model in mobiles:
        del mobiles[model]
        print(f"Deleted mobile: {model}")
    else:
        print(f"Model {model} not found!")

def display():
    global mobiles
    print("\n--- Mobile Phones Database ---")
    for model, specs in mobiles.items():
        print(f"{model}: Price=Rs.{specs['price']}, RAM={specs['ram']}, Storage={specs['storage']}")

# Calling functions
create()
display()
add_mobile("OnePlus 12", 64999, "16GB", "256GB")
update_mobile("iPhone 15", 74900)
display()
delete_mobile("Samsung S24")
display()
