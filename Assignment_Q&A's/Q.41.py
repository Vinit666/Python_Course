"""Q41. Write a program that calculates a person's BMI based on their height
(in meters) and weight (in kilograms). Use the following formula: BMI =
weight / (height^2). Then, classify the BMI according to the following
ranges:
 Underweight: BMI less than 18.5
 Normal weight: BMI 18.5 - 24.9
 Overweight: BMI 25 - 29.9
 Obesity: BMI 30 or greater"""

h = float(input("Enter the height(in meters) : "))
w = float(input("Enter the weight(in kilograms) : "))
bmi = w // (h**2)


if bmi < 18.5:
    print(f"Underweight: BMI {(bmi)} is less than 18.5")
elif bmi >= 18.5 and bmi <= 24.9:
    print(f"Normal weight: BMI {bmi} is between 18.5 - 24.9")
elif bmi >= 25 and bmi <= 29.9:
    print(f"Overweight: BMI {bmi} is between 25 - 29.9")
else:
    print(f"Obesity: BMI {bmi} is 30 or greater")
