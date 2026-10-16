# Program: Reverse Tuple and Strings Inside Tuple
# 1. Print all elements of a tuple in reverse order.
# 2. Take a tuple of string elements and reverse each string element.
#    E.g. ('Pen', 'Marker', 'Pencil') -> ('neP', 'rekraM', 'licneP')

st = ('Pen', 'Marker', 'Pencil', 'Eraser', 'Scale')
print("Original Tuple:", st)

# 1. Reverse tuple order
reversed_tuple = st[::-1]
print("Reversed Tuple Order:", reversed_tuple)

# 2. Reverse each string inside the tuple
rev_strings = []
for item in st:
    rev_strings.append(item[::-1])

rev_strings_tuple = tuple(rev_strings)
print("Each string reversed inside tuple:", rev_strings_tuple)
