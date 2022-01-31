total = int(input("What is the total amount of your bill = "))
tip = int(input("How much do you want to tip = "))
split = int(input("Amongst how many people do you want to split = "))

pay = ((total+((total * tip)/100))/split)
print(f"The amount each person has to pay = " + "{pay}")
