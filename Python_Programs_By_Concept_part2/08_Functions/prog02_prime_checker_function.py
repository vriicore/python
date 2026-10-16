# Program 2.2: Prime Checker Function
# Write a function is_prime(n) that returns True if n is prime, False otherwise.
# Call it for numbers from roll_no to roll_no + 10.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

roll_no = 20
print(f"Checking prime for numbers from {roll_no} to {roll_no + 10}:")
for num in range(roll_no, roll_no + 11):
    result = is_prime(num)
    status = "PRIME" if result else "NOT PRIME"
    print(f"Number {num:<3} -> {status}")
