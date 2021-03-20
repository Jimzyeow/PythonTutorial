# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# separate the input and store in variables, however, it is stored as String, so have to convert into int

column = int(position[0])
row = int(position[1])
print(f"column (horizontal) value is {column} and the type is {type(column)}")
print(f"row (vertical) value is {row} and the type is {type(row)}")

# to summarize, we look at map list, which is the outer list, then to row1, row2, or row3 list, which are nested.

# if user key in 23, column = 2, row = 3. selected_row = map[row-1] --> selected_row = map[2]
# map[2] means map list (map = [row1, row2, row3]) is pointing towards index 2, which is row3
# so back to this line of code: selected_row = map[row-1] is pointing to row3; meaning selected_row = row3
# this line of code: selected_row[column-1] = "X", remember selected_row = row3 and column = 2
# this means inside row3 list, column = 2 is pointing to index 2, the third and last box of row3, so we have to minus 1
# to point to index 1, which is second column.

selected_row = map[row-1]
selected_row[column-1] = "X"

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")