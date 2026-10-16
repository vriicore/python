# Program 3.7: Set Operations Lab
# Create two sets:
# Set 1: Odd numbers 1 to 15 -> {1, 3, 5, 7, 9, 11, 13, 15}
# Set 2: Multiples of 3 up to 15 -> {3, 6, 9, 12, 15}
# Display:
# 1. Union
# 2. Intersection
# 3. Difference (Set 1 - Set 2)
# 4. Difference (Set 2 - Set 1)
# 5. Symmetric Difference

set1 = {x for x in range(1, 16) if x % 2 != 0}
set2 = {x for x in range(1, 16) if x % 3 == 0}

print("Set 1 (Odds 1-15)        :", sorted(set1))
print("Set 2 (Multiples of 3)   :", sorted(set2))

print("\n--- SET OPERATIONS ---")
print("1. Union (Set1 | Set2)               :", sorted(set1.union(set2)))
print("2. Intersection (Set1 & Set2)        :", sorted(set1.intersection(set2)))
print("3. Difference (Set1 - Set2)          :", sorted(set1.difference(set2)))
print("4. Difference (Set2 - Set1)          :", sorted(set2.difference(set1)))
print("5. Symmetric Difference (Set1 ^ Set2):", sorted(set1.symmetric_difference(set2)))
