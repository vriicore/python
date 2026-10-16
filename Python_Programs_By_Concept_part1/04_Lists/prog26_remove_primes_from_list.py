# Program: Remove Prime Numbers From List of 20 Numbers
# Create a list of 20 numbers and remove all prime numbers from the list.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 20 numbers
nums = list(range(1, 21))
print("Original list of 20 numbers:", nums)

non_primes = [x for x in nums if not is_prime(x)]
print("Primes removed (Composite and 1):", non_primes)
