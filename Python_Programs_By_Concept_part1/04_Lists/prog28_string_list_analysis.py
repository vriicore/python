# Program: Analysis on List of Strings
# Display:
# 1. Longest string
# 2. Shortest string
# 3. Strings starting with a vowel
# 4. Strings ending with a consonant

words = ["apple", "banana", "orange", "umbrella", "cat", "egg", "sky"]
print("Word list:", words)

# 1 & 2: longest and shortest
longest = max(words, key=len)
shortest = min(words, key=len)

vowels = ('a', 'e', 'i', 'o', 'u')

# 3: starting with vowel
start_vowel = [w for w in words if w.lower().startswith(vowels)]

# 4: ending with consonant
end_consonant = [w for w in words if not w.lower().endswith(vowels)]

print("Longest string             :", longest)
print("Shortest string            :", shortest)
print("Strings starting with vowel:", start_vowel)
print("Strings ending consonant   :", end_consonant)
