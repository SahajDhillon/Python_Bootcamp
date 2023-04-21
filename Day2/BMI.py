weight = input("What is your weight (KGs) ?")
height = input("What is your height (Ms) ?")
height_float = float(height)
weight_int = int(weight)
BMI = (weight_int / height_float ** 2)
BMI_int = int(BMI)
print(f"Your BMI is {BMI_int}")

