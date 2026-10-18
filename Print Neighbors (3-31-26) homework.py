grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# ask for an input, input will be a value that exists in the grid 
# print out the neighbors of the input value 
# all touching neighbors
value = int(input("Enter a value:"))
neighbors = []
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == value:
            for row_change in [-1, 0, 1]:
                for col_change in [-1, 0, 1]:
                    new_row = row + row_change
                    new_col = col + col_change
                    if row_change == 0 and col_change == 0:
                        continue
                    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[new_row]):
                        neighbors.append(grid[new_row][new_col])

print(neighbors)