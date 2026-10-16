# Program 2.3: Factorial Function
# Write a function factorial(n) using a for loop.
# Call it to display factorials of numbers 1 through 10 in a formatted table.

def factorial(n):
    if n < 0:
        return None
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print("--- FACTORIAL TABLE (1 to 10) ---")
print(f"{'Number (N)':<15}{'Factorial (N!)'}")
print("-" * 30)
for i in range(1, 11):
    print(f"{i:<15}{factorial(i)}")
