# Program: String Concatenation and Repetition
# 1. Take two strings as input from the user and concatenate them.
# 2. Take a number and a string from the user and repeat the string for that many times.

# 1. Concatenation
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
concatenated = str1 + " " + str2
print("Concatenated String:", concatenated)

# 2. Repetition
s = input("\nEnter a string to repeat: ")
times = int(input("Enter number of repetitions: "))
repeated = s * times
print("Repeated String:", repeated)
