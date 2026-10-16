# Program 2.5: String Reverse & Palindrome
# Write reverse_string(s) using slicing.
# Write is_palindrome(s) using the reverse.
# Test with: "madam", "racecar", own name, own city name.

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    clean = s.replace(" ", "").lower()
    return clean == reverse_string(clean)

# Test cases
test_words = ["madam", "racecar", "Vrisha", "Ahmedabad"]

print("--- Palindrome Test ---")
for word in test_words:
    rev = reverse_string(word)
    pal = is_palindrome(word)
    print(f"Word: '{word}' | Reversed: '{rev}' | Is Palindrome: {pal}")
