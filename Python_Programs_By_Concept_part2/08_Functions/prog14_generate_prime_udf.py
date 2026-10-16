# Program: Generate First N Prime Numbers
# Ask total numbers from user and pass in function which will return a list of prime numbers.
# Eg. GeneratePrime(10) returns 1st 10 prime numbers starting from 2.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def GeneratePrime(count):
    primes = []
    current = 2
    while len(primes) < count:
        if is_prime(current):
            primes.append(current)
        current += 1
    return primes

n = 10
first_n_primes = GeneratePrime(n)
print(f"First {n} Prime Numbers:")
print(first_n_primes)
