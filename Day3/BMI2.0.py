weight = input("What is your weight (KGs) ?")
height = input("What is your height (Ms) ?")
height_float = float(height)
weight_int = int(weight)
BMI = (weight_int / height_float ** 2)
BMI_int = int(BMI)
print(f"Your BMI is {BMI_int}")
# print(type(BMI_int))

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
if BMI_int < 18.5:
    print("You are underweight")
elif BMI_int > 18 & BMI_int < 25:
    print("You have a normal weight , Good Job!!")
elif BMI_int > 25 & BMI_int < 30:
    print("You are slightly Overweight ")
elif BMI_int > 30 & BMI_int < 35:
    print("You are Obese")
else:
    print("you are clinically obese")
