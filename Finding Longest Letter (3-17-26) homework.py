grid = [
    ["C", "A", "T", ".", "D", "O", "G"],
    ["B", "A", "L", "L", ".", "A"],
    ["F", "I", "S", "H", "E", "S"],
    ["A", ".", "B", "I", "R", "D"]
]

# find the longest word in this grid 
# . separates two words
# longest letter in this grid is FISHES even though the longest row is row 0 because
# CAT is separated by . from DOG 
longest_word = ""
for row in grid:
    words = "".join(row).split(".")
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
print(f"The longest word in the grid is: {longest_word}")

