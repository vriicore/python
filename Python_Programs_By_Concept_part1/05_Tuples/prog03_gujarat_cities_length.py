# Program: Gujarat Cities Length (With & Without len())
# Create a tuple of cities of Gujarat.
# Find length of each city name with and without len() method.

cities = ("Ahmedabad", "Surat", "Vadodara", "Rajkot", "Gandhinagar", "Bhavnagar")
print("Gujarat Cities:", cities)

print("\n--- City Name Lengths ---")
for city in cities:
    # with len()
    len_builtin = len(city)

    # without len()
    len_manual = 0
    for char in city:
        len_manual += 1

    print(f"City: {city:<15} | Length (len()): {len_builtin} | Length (manual): {len_manual}")
