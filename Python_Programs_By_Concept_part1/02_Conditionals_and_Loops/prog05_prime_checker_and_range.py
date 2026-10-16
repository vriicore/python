# Program 1.17: Prime Number Checker & List
# (a) Take a number and check if it is prime.
# (b) Print all prime numbers from 2 to N. Use a for loop with break.

n = int(input("Enter a number to check prime and print primes up to N: "))

# (a) Checking single number
if n <= 1:
    print(f"{n} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{n} is a Prime Number.")
    else:
        print(f"{n} is not a Prime Number.")

# (b) Print all primes from 2 to N
print(f"\nAll prime numbers from 2 to {n}:")
prime_list = []
for num in range(2, n + 1):
    prime_flag = True
    for d in range(2, int(num**0.5) + 1):
        if num % d == 0:
            prime_flag = False
            break
    if prime_flag:
        prime_list.append(num)

print(prime_list)
