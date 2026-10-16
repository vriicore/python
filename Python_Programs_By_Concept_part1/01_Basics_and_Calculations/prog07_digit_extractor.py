# Program 1.7: Digit Extractor
# Take a 3-digit number as input.
# Extract and display: hundreds digit, tens digit, units digit, sum of digits, product of digits.

num = int(input("Enter a 3-digit number: "))

hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

sum_digits = hundreds + tens + units
prod_digits = hundreds * tens * units

print("Hundreds digit:", hundreds)
print("Tens digit    :", tens)
print("Units digit   :", units)
print("Sum of digits :", sum_digits)
print("Product of digits:", prod_digits)
