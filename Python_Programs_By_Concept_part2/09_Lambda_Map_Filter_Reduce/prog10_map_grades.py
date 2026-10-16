# Program: Calculate Grades for Scores Using map()
# scores = [88, 92, 78, 95, 86] -> ['B', 'A', 'C', 'A', 'B']

scores = [88, 92, 78, 95, 86]

get_grade = lambda score: 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'Fail'
grades = list(map(get_grade, scores))

print("Scores:", scores)
print("Grades:", grades)
