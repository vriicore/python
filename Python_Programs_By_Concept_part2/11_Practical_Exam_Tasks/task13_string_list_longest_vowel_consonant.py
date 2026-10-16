# Practical Exam Task 13:
# Create a list of strings. Display:
# - Longest string
# - Shortest string
# - Strings starting with a vowel
# - Strings ending with a consonant

words = ["apple", "banana", "elephant", "orange", "umbrella", "cat", "sky", "dog"]
print("List of strings:", words)

# Longest and Shortest strings
longest = max(words, key=len)
shortest = min(words, key=len)

vowels = ('a', 'e', 'i', 'o', 'u')

# Strings starting with a vowel
starts_with_vowel = [w for w in words if w.lower().startswith(vowels)]

# Strings ending with a consonant (does not end with vowel)
ends_with_consonant = [w for w in words if not w.lower().endswith(vowels)]

print("\n--- Results ---")
print("Longest String               :", longest)
print("Shortest String              :", shortest)
print("Strings starting with a vowel:", starts_with_vowel)
print("Strings ending with consonant:", ends_with_consonant)
