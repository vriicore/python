# Program 1.4: Temperature Converter
# Take temperature in Celsius as input.
# Convert to Fahrenheit (F = C*9/5 + 32) and Kelvin (K = C + 273.15). Display both.

celsius = float(input("Enter temperature in Celsius: "))

# conversions
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("Temperature in Fahrenheit:", fahrenheit)
print("Temperature in Kelvin:", kelvin)
