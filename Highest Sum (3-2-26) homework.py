grid = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 1, 0]
]

# Print which row has the highest value when all values in the row are added 
max_row_sum = 0
max_row_index = 0
for  max_row in range(len(grid)):
    row_sum = sum(grid[max_row])
    if row_sum > max_row_sum:
        max_row_sum = row_sum
        max_row_index = max_row
print("Row with highest sum is row", max_row_index, "with a sum of", max_row_sum)
max_col_sum = 0
max_col_index = 0
for max_col in range(len(grid[0])):
    col_sum = 0
    for i in range(len(grid)):
        col_sum += grid[i][max_col]
    if col_sum > max_col_sum:
        max_col_sum = col_sum
        max_col_index = max_col
print("Column with highest sum is column", max_col_index, "with a sum of",
    max_col_sum)
# Print which columh has the highest value when all value in the column are added 
