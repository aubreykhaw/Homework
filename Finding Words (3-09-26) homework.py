grid = [
    ["C", "A", "T", "F"],
    ["B", "A", "L", "L"],
    ["D", "O", "G", "S"],
    ["F", "I", "S", "H"]
]

#Enter word: CAT
#Word found at row 0 
input_word = input("Enter a word:").upper()
found = False
for row in grid:
    if input_word in "".join(row):
        print(f"Word found at row {grid.index(row)}")
        found = True
        break
if not found:
    print("Word not found")
#Enter word: DOG
#Word found at row 2 

#Enter a word: WORD
#Word not found