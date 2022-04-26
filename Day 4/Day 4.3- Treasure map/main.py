row1 = ["_", "_", "_"]
row2 = ["_", "_", "_"]
row3 = ["_", "_", "_"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? \n")

row = int(position[0])
column = int(position[1])

map[column-1][row-1] = "X"

print(f"{row1}\n{row2}\n{row3}")

