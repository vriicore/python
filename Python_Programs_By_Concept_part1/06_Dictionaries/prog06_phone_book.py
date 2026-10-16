# Program 3.5: Phone Book Using Dictionary
# Perform:
# (a) Add 5 contacts
# (b) Search by name
# (c) Update a contact number
# (d) Delete a contact
# (e) Display all contacts sorted by name

phone_book = {
    "Vrisha": "9876543210",
    "Aarav": "9123456780",
    "Bina": "9898989898",
    "Diya": "9000011111",
    "Chetan": "9777788888"
}

print("Initial Phone Book:", phone_book)

# (b) Search
name = "Vrisha"
if name in phone_book:
    print(f"Search: {name}'s number is {phone_book[name]}")

# (c) Update
phone_book["Vrisha"] = "9998887776"
print("After update Vrisha's number:", phone_book["Vrisha"])

# (d) Delete
del phone_book["Chetan"]
print("After deleting Chetan:", phone_book)

# (e) Display sorted by name
print("\n--- Phone Book Sorted by Name ---")
for contact in sorted(phone_book.keys()):
    print(f"{contact:<15}: {phone_book[contact]}")
