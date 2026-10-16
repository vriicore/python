# Program 2.9: Anagram Checker
# Write is_anagram(s1, s2) that returns True if two strings are anagrams
# (e.g. 'listen' and 'silent'). Sort both strings and compare. Test 4 pairs.

def is_anagram(s1, s2):
    # remove spaces and convert to lower
    clean1 = sorted(s1.replace(" ", "").lower())
    clean2 = sorted(s2.replace(" ", "").lower())
    return clean1 == clean2

# Testing 4 pairs
test_pairs = [
    ("listen", "silent"),
    ("triangle", "integral"),
    ("apple", "pale"),
    ("race", "care")
]

print("--- Anagram Checker Results ---")
for s1, s2 in test_pairs:
    ans = is_anagram(s1, s2)
    print(f"Are '{s1}' and '{s2}' anagrams? -> {ans}")
