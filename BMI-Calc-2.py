weight = input("Enter your weight = ")
height = input("Enter your height = ")
newWeight = int(weight)
newHeight = float(height)
bmi = (newWeight / (newHeight ** 2))
print(int(bmi))

if bmi>35:
    print("You are Clinically Obese")
elif bmi> 30:
    print("You are Obese")
elif bmi > 25:
    print("You are Overweight")
elif bmi >18.5:
    print("You have a normal Weight")
elif bmi < 18.5:
    print("You are Underweight")