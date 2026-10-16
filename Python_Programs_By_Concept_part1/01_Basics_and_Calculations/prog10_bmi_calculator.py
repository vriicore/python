# Program 1.10: BMI Calculator
# Take weight in kg and height in metres as input.
# Calculate BMI = weight / (height ** 2).
# Display BMI and category: <18.5=Underweight, 18.5-24.9=Normal, 25-29.9=Overweight, >=30=Obese.

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)
print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal"
elif 25 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

print("BMI Category:", category)
