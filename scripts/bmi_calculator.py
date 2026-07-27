height_cm = float(input("Enter your height (cm): "))
weight = float(input("Enter your weight (kg): "))

height_m = height_cm / 100
bmi = weight / (height_m ** 2)

if bmi < 18.5:
    category = "Underweight"
    info = "Your weight is below the healthy range. Consider consulting a nutritionist."
    bmi_range = "Healthy range: 18.5 – 24.9"
elif bmi < 25:
    category = "Normal"
    info = "Your weight is in the healthy range. Keep up your current lifestyle."
    bmi_range = "Healthy range: 18.5 – 24.9"
elif bmi < 30:
    category = "Overweight"
    info = "Your weight is above the healthy range. Regular exercise and a balanced diet may help."
    bmi_range = "Healthy range: 18.5 – 24.9"
else:
    category = "Obese"
    info = "Your weight poses health risks. Consulting a doctor is recommended."
    bmi_range = "Healthy range: 18.5 – 24.9"

print(f"\nBMI: {bmi:.2f} — {category}")
print(f"{bmi_range}")
print(f"Info: {info}")
