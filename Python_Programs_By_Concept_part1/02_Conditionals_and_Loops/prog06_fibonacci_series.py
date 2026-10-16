# Program 1.18: Fibonacci Series
# Print Fibonacci series up to N terms. Each term = sum of previous two (0, 1, 1, 2, 3, 5...).
# Use while loop.

n = int(input("Enter number of terms for Fibonacci series: "))

if n <= 0:
    print("Please enter a positive number of terms.")
elif n == 1:
    print("Fibonacci series: 0")
else:
    a, b = 0, 1
    count = 0
    print("Fibonacci series:")
    while count < n:
        print(a, end=" ")
        nth = a + b
        a = b
        b = nth
        count += 1
    print()
