# Program: Factorial Using Recursive Lambda
# Find factorial of a number using lambda (recursive).

fact = lambda n: 1 if n <= 1 else n * fact(n - 1)

print("Factorial of 0 :", fact(0))
print("Factorial of 1 :", fact(1))
print("Factorial of 5 :", fact(5))
print("Factorial of 7 :", fact(7))
