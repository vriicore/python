# Program 1.15: Multiplication Table
# Take a number N as input.
# Print its multiplication table from 1 to 10 using for loop. Format: "N x 1 = N".

n = int(input("Enter number for multiplication table: "))

print(f"--- Multiplication Table for {n} ---")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
