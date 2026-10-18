grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# output a grid that prints the rows backwards 

# output grid = [
#     [3, 2, 1],
#     [6, 5, 4],
#     [9, 8, 7]
new_grid = []

for row in grid:
    new_row = []
    for i in range(len(row) - 1, -1, -1):
        new_row.append(row[i])
    new_grid.append(new_row)

# print nicely
for row in new_grid:
    print(row)