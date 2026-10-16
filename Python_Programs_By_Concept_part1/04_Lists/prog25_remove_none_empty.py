# Program: Remove None and Empty Values From List
# Clean a list by filtering out None, empty strings, and empty sublists.

dirty_list = ["apple", "", None, "banana", "   ", None, "cherry", []]
print("Original list:", dirty_list)

cleaned = []
for item in dirty_list:
    # check if not None and not empty string (ignoring whitespace)
    if item is not None and item != "" and item != "   " and item != []:
        cleaned.append(item)

print("Cleaned list :", cleaned)
