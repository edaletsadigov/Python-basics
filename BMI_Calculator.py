# BMI Calculator
# Calculates Body Mass Index and shows the weight category

height_cm = float(input("Enter your height (cm): "))
weight = float(input("Enter your weight (kg): "))

height_m = height_cm / 100
bmi = weight / (height_m ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi:.2f} — {category}")