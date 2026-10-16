# Program 2.11: Default Parameter Function
# Write a function display_info(name, city="Ahmedabad", programme="M.Sc. IT")
# Call it:
# (a) with all 3 arguments
# (b) with only name
# (c) with name and city

def display_info(name, city="Ahmedabad", programme="M.Sc. IT"):
    print(f"Student: {name:<12} | City: {city:<12} | Programme: {programme}")

print("--- Calling Function with Default Parameters ---")
print("(a) All 3 arguments:")
display_info("Vrisha", "Surat", "MCA")

print("\n(b) Only name argument:")
display_info("Aarav")

print("\n(c) Name and city arguments:")
display_info("Bhavya", "Vadodara")
