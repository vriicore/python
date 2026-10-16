# Program: Count Vowels Using Tuple of Vowels
# Take a string input from user. Find total number of vowels in it.
# Hint: Use a tuple of vowels.

user_input = input("Enter a sentence: ")
vowels_tuple = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

vowel_count = 0
found_vowels = []

for ch in user_input:
    if ch in vowels_tuple:
        vowel_count += 1
        found_vowels.append(ch)

print(f"Total number of vowels found: {vowel_count}")
print("Vowels found:", found_vowels)
