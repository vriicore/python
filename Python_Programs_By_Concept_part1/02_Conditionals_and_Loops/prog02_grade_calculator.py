# Program 1.14: Grade Calculator
# Take marks as input.
# Display grade using if-elif-else:
# >=90 = A+, >=80 = A, >=70 = B, >=60 = C, >=35 = D, else = Fail
# Also display "Distinction" if marks >= 90.

marks = float(input("Enter student marks (0 - 100): "))

if marks < 0 or marks > 100:
    print("Invalid marks entered! Please enter between 0 and 100.")
else:
    if marks >= 90:
        grade = "A+"
        print("Congratulations! Distinction achieved.")
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 35:
        grade = "D"
    else:
        grade = "Fail"

    print("Final Grade:", grade)
