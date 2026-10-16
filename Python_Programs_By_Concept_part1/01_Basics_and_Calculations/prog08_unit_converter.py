# Program 1.8: Unit Converter
# Take a distance in kilometres as input.
# Convert to: metres (*1000), centimetres (*100000), miles (*0.621371), feet (*3280.84).

km = float(input("Enter distance in kilometers: "))

meters = km * 1000
centimeters = km * 100000
miles = km * 0.621371
feet = km * 3280.84

print("Distance in Metres      :", meters)
print("Distance in Centimetres :", centimeters)
print("Distance in Miles       :", miles)
print("Distance in Feet        :", feet)
