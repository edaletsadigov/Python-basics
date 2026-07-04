# BMI Calculator

Calculates Body Mass Index based on height and weight, then prints the weight category.

## How it works

1. User enters height in cm and weight in kg
2. Script converts height to meters and applies the BMI formula
3. Result is classified using standard WHO thresholds

**Formula:** `BMI = weight (kg) / height (m)²`

| BMI | Category |
|-----|----------|
| < 18.5 | Underweight |
| 18.5 – 24.9 | Normal |
| 25.0 – 29.9 | Overweight |
| ≥ 30.0 | Obese |

## Run

```bash
python bmi_calculator.py
```

## Example

```
Enter your height (cm): 175
Enter your weight (kg): 70
BMI: 22.86 — Normal
```

## Requirements

Python 3.x — no external libraries needed.
