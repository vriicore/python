# Program 1.3: Simple Interest Calculator
# Take Principal (P), Rate (R), and Time (T) as input.
# Calculate SI = P*R*T/100. Display SI and the total amount (P+SI).

p = float(input("Enter Principal amount (P): "))
r = float(input("Enter Rate of interest (R): "))
t = float(input("Enter Time in years (T): "))

# formula for simple interest
si = (p * r * t) / 100
total_amount = p + si

print("Simple Interest =", si)
print("Total Amount =", total_amount)
