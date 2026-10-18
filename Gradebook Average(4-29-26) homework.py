# Input:
# Enter student name: Alice
# Enter score: 90

# Enter student name: Alice
# Enter score: 80

# Enter student name: Bob
# Enter score: 70

# Enter student name: done

# Output: 
# Alice: [90, 80]
# Average: 85

# Bob: [70]
# Average: 70
gradebook = {}
while True:
    name = input("Enter student name: ")
    if name.lower() == "done":
        break
    score = int(input("Enter score: "))
    
    if name in gradebook:
        gradebook[name].append(score)
    else:
        gradebook[name] = [score]
for student, scores in gradebook.items():
    average = sum(scores) / len(scores)
    print(f"{student}: {scores}")
    print(f"Average: {average}")