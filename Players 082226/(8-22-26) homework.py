import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# --------------------------------------------
# LOAD TOURNAMENT DATA
# --------------------------------------------

try:
    file_path = os.path.join(BASE_DIR, "tournament.json")
    with open(file_path, "r") as file:
        players = json.load(file)
except FileNotFoundError:
    players = {}


# --------------------------------------------
# SAVE TOURNAMENT DATA
# --------------------------------------------

def save_players():
    file_path = os.path.join(BASE_DIR, "tournament.json")
    with open(file_path, "w") as file:
        json.dump(players, file, indent=4)

# --------------------------------------------
# VIEW PLAYERS
# --------------------------------------------

def view_players():
    if len(players) == 0:
        print("No players.")
    else:
        for name, score in players.items():
            print(name + ": " + str(score) + " points")


# --------------------------------------------
# ADD PLAYER
# --------------------------------------------

def add_player():
    name = input("Enter player name: ").strip()

    if name == "":
        print("Player name cannot be empty.")
    elif name in players:
        print("Player already exists.")
    else:
        players[name] = 0
        save_players()
        print(name + " has been added.")


# --------------------------------------------
# ADD POINTS
# --------------------------------------------

def add_points():
    name = input("Enter player name: ").strip()

    if name not in players:
        print("Player does not exist.")
        return

    try:
        points = int(input("Enter points to add: "))

        if points <= 0:
            print("Points must be greater than 0.")
        else:
            players[name] += points
            save_players()
            print(name + " now has " + str(players[name]) + " points.")

    except ValueError:
        print("Please enter a valid number.")


# --------------------------------------------
# REMOVE PLAYER
# --------------------------------------------

def remove_player():
    name = input("Enter player name: ").strip()

    if name not in players:
        print("Player does not exist.")
    else:
        del players[name]
        save_players()
        print(name + " has been removed.")


# --------------------------------------------
# SHOW LEADER
# --------------------------------------------

def show_leader():
    if len(players) == 0:
        print("There are no players.")
    else:
        leader = max(players, key=players.get)
        print("Leader: " + leader)
        print("Score: " + str(players[leader]))


# --------------------------------------------
# SHOW TOP 3
# --------------------------------------------

def show_top_3():
    if len(players) == 0:
        print("There are no players.")
        return

    # sorted_players = sorted(players.items(), key=lambda item: item[1], reverse=True)
    # item -> 'aubrey', 5
    # item[0] -> 'aubrey'
    # item[1] -> 5 

    highest = ""
    score = 0
    for name in players:
        if players[name] > score:
            highest = name
            score = players[name]

    # second_highest will be equal to or less than the first highest 
    
    sec_highest = ""
    second_score = 0
    for name in players:
        if players[name] > second_score and players[name] < score:
            sec_highest = name
            second_score = players[name]

  

    third_highest = ""
    third_score = 0
    for name in players:
        if players[name] > third_score and players[name] < second_score:
            third_highest = name
            third_score = players[name]
    print("Leader: "+ highest + " - " + str(score))
    print("Second: "+ sec_highest + " - " + str(second_score))
    print("Third: "+ third_highest + " - " + str(third_score))

    # for i, (name, score) in enumerate(sorted_players[:3], start=1):
    #     print(str(i) + ". " + name + " - " + str(score))


# --------------------------------------------
# SHOW AVERAGE SCORE
# --------------------------------------------

def show_average():
    if len(players) == 0:
        print("There are no players.")
    else:
        average = sum(players.values()) / len(players)
        print("Average score: " + str(round(average, 2)))


# --------------------------------------------
# SORT PLAYERS
# --------------------------------------------

def sort_players():
    if len(players) == 0:
        print("There are no players.")
        return

    sorted_players = sorted(players.items(), key=lambda item: item[1], reverse=True)

    for name, score in sorted_players:
        print(name + ": " + str(score))


# --------------------------------------------
# RESET SCORES
# --------------------------------------------

def reset_scores():
    for name in players:
        players[name] = 0

    save_players()
    print("All scores have been reset.")


# --------------------------------------------
# MAIN MENU
# --------------------------------------------

while True:

    print("\n===== TOURNAMENT MANAGER =====")
    print("1. View Players")
    print("2. Add Player")
    print("3. Add Points")
    print("4. Remove Player")
    print("5. Show Leader")
    print("6. Show Top 3")
    print("7. Show Average Score")
    print("8. Sort Players")
    print("9. Reset Scores")
    print("10. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        view_players()

    elif choice == "2":
        add_player()

    elif choice == "3":
        add_points()

    elif choice == "4":
        remove_player()

    elif choice == "5":
        show_leader()

    elif choice == "6":
        show_top_3()

    elif choice == "7":
        show_average()

    elif choice == "8":
        sort_players()

    elif choice == "9":
        reset_scores()

    elif choice == "10":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1-10.")