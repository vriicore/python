# Program: Segregate Odd and Even into 2 Different Tuples
# Take a tuple of 10 integer numbers and segregate odd and even numbers into 2 different tuples.

numbers = (14, 25, 33, 42, 50, 61, 78, 89, 90, 95)
print("Original Numbers Tuple:", numbers)

even_list = []
odd_list = []

for n in numbers:
    if n % 2 == 0:
        even_list.append(n)
    else:
        odd_list.append(n)

# converting back to tuples
even_tuple = tuple(even_list)
odd_tuple = tuple(odd_list)

print("Even Numbers Tuple:", even_tuple)
print("Odd Numbers Tuple :", odd_tuple)
