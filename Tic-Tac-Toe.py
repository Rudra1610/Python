row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
print("(input example = 2,3)")
givenPos = input("Where do you want to put the treasure = ")
pos = givenPos.split(",")
print(pos)
print(map[pos])
print(f"{row1}\n{row2}\n{row3}")