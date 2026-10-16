# Program: Lambda Conditional Product or Concatenation
# Takes 2 inputs: If inputs are integers, return product, else concatenation.

calc = lambda a, b: a * b if (isinstance(a, int) and isinstance(b, int)) else str(a) + str(b)

print("Integers (5, 6)       :", calc(5, 6))
print("Strings ('Hello', 'World'):", calc("Hello ", "World"))
print("Mixed (10, 'Apples')  :", calc(10, " Apples"))
