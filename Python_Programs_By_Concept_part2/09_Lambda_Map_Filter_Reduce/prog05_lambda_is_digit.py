# Program: Check Digits Using Lambda
# Create a list of mixed inputs and write a lambda function to check whether element is digit.
# Eg. ['1', '2', 'a', 'b', '3', 'c'] -> [True, True, False, False, True, False]

elements = ['1', '2', 'a', 'b', '3', 'c', 'd', '10']
is_digit_lambda = lambda s: str(s).isdigit()

results = list(map(is_digit_lambda, elements))
print("Original List :", elements)
print("Is Digit List :", results)
