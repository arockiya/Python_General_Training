# 2_Dimensisonal List
# Lists within list

number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(number_grid)

# print one value from the grid: Value 3
print(number_grid[0][2])

# print one value from the grid: Value 8
print(number_grid[2][1])

# Nested loops to use in 2D lists
# To print ll the values inside the number grid

for row in number_grid:
    for col in row:
        print(col)
