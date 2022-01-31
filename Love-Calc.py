print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combinedName = (name1 + name2).lower()
t = combinedName.count("t")
r = combinedName.count("r")
u = combinedName.count("u")
e = combinedName.count("e")

true = t + r + u + e

l = combinedName.count("l")
o = combinedName.count("o")
v = combinedName.count("v")
e = combinedName.count("e")

love = l + o + v + e
score = str(true)+str(love)
print(f"Score: {score}")