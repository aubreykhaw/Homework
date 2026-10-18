grid = [
    ["A", "B", "C"],
    ["D", "X", "E"],
    ["F", "G", "H"]
]
# do the same as last week but try writing without emnumbrate
for row_index in range(len(grid)):
    row = grid[row_index]
    for col_index in range(len(row)):
        value = row[col_index]
        if value == "X":
            print(f"X found at row {row_index}, column {col_index}")
