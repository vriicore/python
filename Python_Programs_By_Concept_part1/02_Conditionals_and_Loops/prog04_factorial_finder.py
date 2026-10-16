# Program 1.16: Factorial Finder
# Take a number N as input.
# Calculate its factorial using for loop (e.g., 5! = 120).
# Handle N=0 and N=1 correctly.

n = int(input("Enter a non-negative number: "))

if n < 0:
    print("Factorial does not exist for negative numbers!")
elif n == 0 or n == 1:
    print(f"Factorial of {n} is 1")
else:
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    print(f"Factorial of {n} is {fact}")
