# Program 1.21: Armstrong Number Finder
# Check if a number is Armstrong (e.g., 153 = 1^3 + 5^3 + 3^3).
# Then print all Armstrong numbers between 1 and 999.

# (a) Check given number
num = int(input("Enter a number to check if it is Armstrong: "))
temp = num
num_digits = len(str(num))
sum_pow = 0

while temp > 0:
    digit = temp % 10
    sum_pow += digit ** num_digits
    temp //= 10

if sum_pow == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")

# (b) Print all Armstrong numbers from 1 to 999
print("\nAll Armstrong numbers between 1 and 999:")
armstrong_list = []
for n in range(1, 1000):
    t = n
    digits = len(str(n))
    s = 0
    while t > 0:
        d = t % 10
        s += d ** digits
        t //= 10
    if s == n:
        armstrong_list.append(n)

print(armstrong_list)
