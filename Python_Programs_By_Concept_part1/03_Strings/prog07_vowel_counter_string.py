# Program: Vowel Counter in String
# Check if any vowel is present in the given string.
# If present, count each vowel (a, e, i, o, u) and display total number of vowels.

text = input("Enter a string: ")
text_lower = text.lower()

vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
total_vowels = 0

for ch in text_lower:
    if ch in vowels:
        vowels[ch] += 1
        total_vowels += 1

if total_vowels > 0:
    print(f"Vowels are present! Total count = {total_vowels}")
    print("Individual counts:")
    for v, c in vowels.items():
        print(f"  '{v}': {c}")
else:
    print("No vowels found in the string.")
