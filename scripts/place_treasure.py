#Understanding 2-D Arrays
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


y_coordinate = int(position[0]) - 1
x_coordinate = int(position[1]) - 1

map[x_coordinate][y_coordinate] = "X"

#Print the rows again with X marking the treasure again.
print(f"{row1}\n{row2}\n{row3}")