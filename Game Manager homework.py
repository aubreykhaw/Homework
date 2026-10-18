# ============================================
# Homework Assignment: Game Save Manager
# ============================================
#
# Objective:
# Practice using lists and dictionaries to
# manage player profiles and game progress.
#
# --------------------------------------------
# DATA STRUCTURE
# --------------------------------------------
#
# Example:
#
# players = [
#     {
#         "name": "Alex",
#         "level": 5,
#         "health": 80,
#         "coins": 250
#     },
#     {
#         "name": "Sam",
#         "level": 3,
#         "health": 100,
#         "coins": 120
#     }
# ]
#
# Each player is stored as a dictionary
# inside a list.
#
# --------------------------------------------
# MENU OPTIONS
# --------------------------------------------
#
# 1. View Players
# 2. Create Player
# 3. Level Up Player
# 4. Add Coins
# 5. Take Damage
# 6. Delete Player
# 7. Find Strongest Player
# 8. Exit
#
# --------------------------------------------
# REQUIREMENTS
# --------------------------------------------
#
# 1. VIEW PLAYERS
# ----------------
# Display all players and their stats.
#
# Example:
#
# Alex
# Level: 5
# Health: 80
# Coins: 250
#
#
# 2. CREATE PLAYER
# -----------------
# Ask for:
# - player name
#
# New players should start with:
# - Level: 1
# - Health: 100
# - Coins: 0
#
# Add the player to the list.
#
# If the player already exists:
# - print an error message
#
#
# 3. LEVEL UP PLAYER
# -------------------
# Ask for:
# - player name
#
# Increase the player's level by 1.
#
#
# 4. ADD COINS
# -------------
# Ask for:
# - player name
# - amount of coins
#
# Increase the player's coins.
#
#
# 5. TAKE DAMAGE
# ---------------
# Ask for:
# - player name
# - damage amount
#
# Decrease health.
#
# Requirements:
# - Health cannot go below 0
#
#
# 6. DELETE PLAYER
# -----------------
# Ask for:
# - player name
#
# Remove the player from the list.
#
#
# 7. FIND STRONGEST PLAYER
# -------------------------
# Find and display:
# - player name
# - level
#
# The strongest player is the player
# with the highest level.
#
#
# 8. EXIT
# --------
# End the program.
#
#
# --------------------------------------------
# PROGRAM REQUIREMENTS
# --------------------------------------------
#
# - Use functions
# - Use a while loop
# - Use a list of dictionaries
# - Use loops to search through players
# - Validate user input
players = []

def view_players():
    if len(players) == 0:
        print("No players found.")
    else:
        for player in players:
            print("\n------------------")
            print(player["name"])
            print("Level:", player["level"])
            print("Health:", player["health"])
            print("Coins:", player["coins"])
            print("------------------")


def create_player():
    name = input("Enter player name: ")

    for player in players:
        if player["name"].lower() == name.lower():
            print("Player already exists.")
            return

    new_player = {
        "name": name,
        "level": 1,
        "health": 100,
        "coins": 0
    }

    players.append(new_player)
    print("Player created successfully!")


def level_up_player():
    name = input("Enter player name: ")

    for player in players:
        if player["name"].lower() == name.lower():
            player["level"] += 1
            print(player["name"], "leveled up!")
            return

    print("Player not found.")


def add_coins():
    name = input("Enter player name: ")

    for player in players:
        if player["name"].lower() == name.lower():
            try:
                coins = int(input("Enter amount of coins: "))

                if coins < 0:
                    print("Amount must be positive.")
                    return

                player["coins"] += coins
                print("Coins added!")
                return

            except:
                print("Invalid amount.")
                return

    print("Player not found.")


def take_damage():
    name = input("Enter player name: ")

    for player in players:
        if player["name"].lower() == name.lower():
            try:
                damage = int(input("Enter damage amount: "))

                if damage < 0:
                    print("Damage must be positive.")
                    return

                player["health"] -= damage

                if player["health"] < 0:
                    player["health"] = 0

                print(player["name"], "now has", player["health"], "health.")
                return

            except:
                print("Invalid damage amount.")
                return

    print("Player not found.")


def delete_player():
    name = input("Enter player name: ")

    for player in players:
        if player["name"].lower() == name.lower():
            players.remove(player)
            print("Player deleted.")
            return

    print("Player not found.")


def find_strongest_player():
    if len(players) == 0:
        print("No players found.")
        return

    strongest = players[0]

    for player in players:
        if player["level"] > strongest["level"]:
            strongest = player

    print("\nStrongest Player")
    print("----------------")
    print("Name:", strongest["name"])
    print("Level:", strongest["level"])


while True:

    print("\n===== Game Save Manager =====")
    print("1. View Players")
    print("2. Create Player")
    print("3. Level Up Player")
    print("4. Add Coins")
    print("5. Take Damage")
    print("6. Delete Player")
    print("7. Find Strongest Player")
    print("8. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        view_players()

    elif choice == "2":
        create_player()

    elif choice == "3":
        level_up_player()

    elif choice == "4":
        add_coins()

    elif choice == "5":
        take_damage()

    elif choice == "6":
        delete_player()

    elif choice == "7":
        find_strongest_player()

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")