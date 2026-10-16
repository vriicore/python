# Program: Average with Variable Length Arguments (*args)
# Find the average of all elements passed as an argument in lambda.

avg = lambda *args: sum(args) / len(args) if args else 0

print("Average of (10, 20, 30)            :", avg(10, 20, 30))
print("Average of (5, 10, 15, 20, 25, 30) :", avg(5, 10, 15, 20, 25, 30))
