# Program 1.20: Star Pattern Collection
# Print three patterns:
# (a) Right-angled triangle (5 rows)
# (b) Inverted triangle (5 rows)
# (c) Diamond pattern (5 rows)
# All using nested loops.

rows = 5

print("--- (a) Right-Angled Triangle ---")
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n--- (b) Inverted Triangle ---")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n--- (c) Diamond Pattern ---")
# Upper half
for i in range(1, rows + 1):
    for space in range(rows - i):
        print(" ", end="")
    for star in range(2 * i - 1):
        print("*", end="")
    print()

# Lower half
for i in range(rows - 1, 0, -1):
    for space in range(rows - i):
        print(" ", end="")
    for star in range(2 * i - 1):
        print("*", end="")
    print()
