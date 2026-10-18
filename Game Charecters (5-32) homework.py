# ============================================
# Homework Assignment: RPG Character Manager
# ============================================
#
# Objective:
# Practice using dictionaries to manage
# RPG characters and their stats.
#
# --------------------------------------------
# DATA STRUCTURE
# --------------------------------------------
#
# Example:
#
# characters = {
#     "Knight": 100,
#     "Wizard": 80,
#     "Archer": 90
# }
#
# Keys are character names.
# Values are health points (HP).
#
# --------------------------------------------
# MENU OPTIONS
# --------------------------------------------
#
# 1. View Characters
# 2. Create Character
# 3. Heal Character
# 4. Damage Character
# 5. Delete Character
# 6. Find Strongest Character
# 7. Battle Two Characters
# 8. Exit
#
# --------------------------------------------
# REQUIREMENTS
# --------------------------------------------
#
# 1. VIEW CHARACTERS
# -------------------
# Display all characters and their HP.
#
#
# 2. CREATE CHARACTER
# --------------------
# Ask the user for:
# - character name
# - starting HP
#
# Add the character to the dictionary.
#
# If the character already exists:
# - print an error message
#
#
# 3. HEAL CHARACTER
# ------------------
# Ask for:
# - character name
# - amount to heal
#
# Increase the character's HP.
#
#
# 4. DAMAGE CHARACTER
# --------------------
# Ask for:
# - character name
# - damage amount
#
# Decrease the character's HP.
#
# HP cannot go below 0.
#
#
# 5. DELETE CHARACTER
# --------------------
# Remove a character from the dictionary.
#
#
# 6. FIND STRONGEST CHARACTER
# ----------------------------
# Find the character with the highest HP.
#
#
# 7. BATTLE TWO CHARACTERS
# -------------------------
# Ask for:
# - attacker
# - defender
#
# The attacker deals 10 damage.
#
# Example:
# Knight attacks Wizard!
# Wizard loses 10 HP.
#
# If HP reaches 0:
# Wizard has been defeated!
#
#
# 8. EXIT
# --------
# End the program.

characters = {}
character_names = []
character_hp = []
running = True
while running:
    menu_option = input("Choose an option: view, create, heal, damage, delete, strongest, battle, exit: ")
    
    if menu_option == "view":
        for character in characters:
            print(character + ": " + str(characters[character]) + " HP")
    
    elif menu_option == "create":
        name = input("Enter character name: ")
        hp = int(input("Enter starting HP: "))
        
        if name in characters:
            print("Character already exists!")
        else:
            characters[name] = hp
            print(f"{name} created with {hp} HP.")
    
    elif menu_option == "heal":
        name = input("Enter character name to heal: ")
        amount = int(input("Enter amount to heal: "))
        
        if name in characters:
            characters[name] += amount
            print(f"{name} healed by {amount}. Current HP: {characters[name]}")
        else:
            print("Character not found!")
    
    elif menu_option == "damage":
        name = input("Enter character name to damage: ")
        amount = int(input("Enter damage amount: "))
        
        if name in characters:
            characters[name] -= amount
            if characters[name] < 0:
                characters[name] = 0
            print(f"{name} damaged by {amount}. Current HP: {characters[name]}")
        else:
            print("Character not found!")
    
    elif menu_option == "delete":
        name = input("Enter character name to delete: ")
        
        if name in characters:
            del characters[name]
            print(f"{name} has been deleted.")
        else:
            print("Character not found!")
    
    elif menu_option == "strongest":
        if characters:
            strongest = max(characters, key=characters.get)
            print(f"The strongest character is {strongest} with {characters[strongest]} HP.")
        else:
            print("No characters available!")
    
    elif menu_option == "battle":
        attacker = input("Enter attacker name: ")
        defender = input("Enter defender name: ")
        
        if attacker in characters and defender in characters:
            print(f"{attacker} attacks {defender}!")
            characters[defender] -= 10
            if characters[defender] < 0:
                characters[defender] = 0
                print(f"{defender} has been defeated!")
            else:
                print(f"{defender} loses 10 HP. Current HP: {characters[defender]}")
        else:
            print("One or both characters not found!")
    elif menu_option == "exit":
        running = False
        print("Exiting the program. Goodbye!")
