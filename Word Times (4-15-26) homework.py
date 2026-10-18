# Use a dictionary to determine how many times a word appears in the words list 

# Expected output: 

# apple: 3
# banana: 2
# orange: 1

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1
for word in word_count:
    print(word + ": " + str(word_count[word]))

