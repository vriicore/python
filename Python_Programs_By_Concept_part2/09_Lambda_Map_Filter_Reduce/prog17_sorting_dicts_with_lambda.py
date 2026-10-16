# Program: Sort Dictionaries Using Lambda
# 1. Sort students by age, and if age is same then sort by name
# 2. Sort phone models by model number

students = [
    {'name': 'Amit', 'age': 25},
    {'name': 'Bina', 'age': 22},
    {'name': 'Dax', 'age': 25},
    {'name': 'Aarav', 'age': 22}
]

models = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# 1. Sort by age, then name
sorted_students = sorted(students, key=lambda x: (x['age'], x['name']))

# 2. Sort phone models by integer model number
sorted_models = sorted(models, key=lambda x: int(x['model']))

print("Sorted Students (Age then Name):")
for s in sorted_students:
    print(" ", s)

print("\nSorted Phone Models (by model number):")
for m in sorted_models:
    print(" ", m)
