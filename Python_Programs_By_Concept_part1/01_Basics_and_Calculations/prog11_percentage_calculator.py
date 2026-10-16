# Program 1.11: Percentage Calculator
# Take marks in 5 subjects as input.
# Calculate total, percentage (out of 500), and average. Display all.

m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))
m4 = float(input("Enter marks in Subject 4: "))
m5 = float(input("Enter marks in Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100
average = total / 5

print("Total Marks (out of 500) =", total)
print("Percentage =", percentage, "%")
print("Average Marks =", average)
