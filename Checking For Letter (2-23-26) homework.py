# The user will input a letter 
# Check if the letter exists in the grid 
# If it does, print the coordinates of where it is in the grid 
# If it is not in the grid, print 'not found' 

grid = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
]
letter = input("Enter a letter: ")
found = False
for row in range(len(grid)):
    for column in range(len(grid[row])):
        if grid[row][column] == letter:
            print(f"Letter found at coordinates: ({row}, {column})")
            found = True
        break
    if not found:
        break
        print("Letter not found in the grid.")
