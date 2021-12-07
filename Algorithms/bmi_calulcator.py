height = float(input("Provide your height (example: 1.80): \n"))
weight = int(input("Provide weight: \n"))

bmi = float(weight / (height) ** 2)
good_start_weight = 18.50*(height**2)
good_end_weight = 24.99*(height**2)

if bmi >= 40.00:
    diagnosis = "Diagnosis: III Overweight" 
elif bmi < 16.00:
    diagnosis = "Diagnosis: Starving"
elif bmi > 16.00 and bmi <= 16.99:
    diagnosis = "Diagnosis: Emaciation"
elif bmi > 17.00 and bmi <= 18.49:
    diagnosis = "Diagnosis: Underweight"
elif bmi > 18.50 and bmi <= 24.99:
    diagnosis = "Diagnosis: Correct weight"
elif bmi > 25.00 and bmi <= 29.99:
    diagnosis = "Diagnosis: Overweight"
elif bmi > 30.00 and bmi <= 34.99:
    diagnosis = "Diagnosis: 1 Overweight"
elif bmi > 35.00 and bmi <= 39.99:
    diagnosis = "Diagnosis: 2 Overweight"

print(f"Your BMI is: {bmi:.2f}. {diagnosis}. Your correct weight is: {good_start_weight:.1f} - {good_end_weight:.1f}")