grid = [
    ["A", "B", "C"],
    ["D", "X", "E"],
    ["F", "G", "H"]
]
# Ask user for row
row = int(input("Enter row number (0-2): "))
# Ask user for column
col = int(input("Enter column number (0-2): "))
# Get value at specified position
value = grid[row][col]
print(f"Value at ({row}, {col}): {value}")