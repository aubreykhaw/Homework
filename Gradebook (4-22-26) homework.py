# Gradebook (Must use dictionary)

# Input:
# Enter student name: Alice
# Enter score: 90

# Enter student name: Bob
# Enter score: 85

# Enter student name: Charlie
# Enter score: 95

# Enter student name: done

# Output: 
# Alice: 90
# Bob: 85
# Charlie: 95

# Top student: Charlie
# Score: 95
gradebook = {}
while True:
    name = input("Enter student name: ")
    if name == "done":
        break
    score = int(input("Enter score: "))
    gradebook[name] = score
for student, score in gradebook.items():
    print(f"{student}: {score}")
top_student = max(gradebook, key=gradebook.get)
print(f"Top student: {top_student}")
print(f"Score: {gradebook[top_student]}")
