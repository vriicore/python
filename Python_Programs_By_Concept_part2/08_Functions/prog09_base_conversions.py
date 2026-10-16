# Program: Number Base Conversions
# Create functions to convert decimal numbers to binary, octal, and hexadecimal numbers.
# Always return values from the functions.

def to_binary(n):
    return bin(n)[2:]

def to_octal(n):
    return oct(n)[2:]

def to_hexadecimal(n):
    return hex(n)[2:].upper()

num = 156
print(f"Decimal Number: {num}")
print("Binary representation     :", to_binary(num))
print("Octal representation      :", to_octal(num))
print("Hexadecimal representation:", to_hexadecimal(num))
