# Program 3.11: Inventory System
# Build a simple inventory using dictionary: product_name -> quantity.
# Functions: add_item, remove_item, update_qty, display_inventory, low_stock (qty < 5).

inventory = {
    "Notebook": 20,
    "Pen": 50,
    "Pencil": 4,
    "Eraser": 3,
    "Highlighter": 12
}

def add_item(item, qty):
    inventory[item] = inventory.get(item, 0) + qty
    print(f"Added {qty} of '{item}'.")

def remove_item(item):
    if item in inventory:
        del inventory[item]
        print(f"Item '{item}' removed from inventory.")
    else:
        print("Item not found!")

def update_qty(item, qty):
    if item in inventory:
        inventory[item] = qty
        print(f"Updated '{item}' quantity to {qty}.")
    else:
        print("Item not found!")

def display_inventory():
    print("\n--- Current Inventory ---")
    for item, qty in inventory.items():
        print(f"{item:<15}: {qty} units")

def low_stock():
    print("\n--- Low Stock Alert (Quantity < 5) ---")
    for item, qty in inventory.items():
        if qty < 5:
            print(f"WARNING: '{item}' has only {qty} units remaining!")

# Demonstration
display_inventory()
add_item("Ruler", 15)
update_qty("Notebook", 25)
low_stock()
