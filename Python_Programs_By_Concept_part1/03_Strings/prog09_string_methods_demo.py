# Program 2.8: String Methods Practice
# Take a sentence as input. Apply and display:
# (a) upper()
# (b) lower()
# (c) title()
# (d) strip()
# (e) split() - display list of words
# (f) replace all spaces with "_"
# (g) find("a") - first occurrence

sentence = input("Enter a sentence with spaces: ")

print("\n--- String Methods Results ---")
print("(a) upper()                  :", sentence.upper())
print("(b) lower()                  :", sentence.lower())
print("(c) title()                  :", sentence.title())
print("(d) strip()                  :", sentence.strip())
print("(e) split()                  :", sentence.split())
print("(f) spaces replaced with '_' :", sentence.replace(" ", "_"))
print("(g) find('a') first index    :", sentence.find("a"))
