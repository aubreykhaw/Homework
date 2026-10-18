grid = [
    ["A", "B", "C"],
    ["D", "X", "E"],
    ["F", "G", "X"]
]

for row_index, row in enumerate(grid):
    for col_index, value in enumerate(row):
        if value == "X":
            print(f"X found at row {row_index}, column {col_index}")

