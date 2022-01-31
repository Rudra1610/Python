import random

# giveName = input("Enter all names seperated by a comma: ")
# friends = giveName.split(',')
rand = random.randint(0, 3)
friends = ["Rudra", "Tisha", "Crazy Monkey", "Ugly Donkey"]

def bankerRoulette():
    print(friends[rand])

bankerRoulette()
print("hello")