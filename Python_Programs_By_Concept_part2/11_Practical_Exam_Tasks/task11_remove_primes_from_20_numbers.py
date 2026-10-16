# Practical Exam Task 11:
# Create a list of 20 numbers and remove all prime numbers from the list.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# list of 20 numbers from 1 to 20
numbers = list(range(1, 21))
print("Original list of 20 numbers:")
print(numbers)

# remove prime numbers
non_primes = []
primes_removed = []

for num in numbers:
    if is_prime(num):
        primes_removed.append(num)
    else:
        non_primes.append(num)

print("\nPrimes that were removed:", primes_removed)
print("Final list after removing all primes:", non_primes)
