# ============================================
# Homework Assignment: Banking System
# ============================================
#
# Objective:
# Practice using dictionaries, functions,
# loops, and conditionals to build a simple
# banking system.
#
# --------------------------------------------
# DATA STRUCTURE
# --------------------------------------------
#
# Example:
#
# accounts = {
#     "alice": 500,
#     "bob": 1200,
#     "charlie": 300
# }
#
# Keys are account usernames.
# Values are account balances.
#
# --------------------------------------------
# MENU OPTIONS
# --------------------------------------------
#
# 1. View All Accounts
# 2. Create Account
# 3. Deposit Money
# 4. Withdraw Money
# 5. Transfer Money
# 6. Delete Account
# 7. Find Richest Account
# 8. Exit
#
# The program should continuously run in a
# while loop until the user chooses Exit.
#
# --------------------------------------------
# REQUIREMENTS
# --------------------------------------------
#
# 1. VIEW ALL ACCOUNTS
# ---------------------
# Display all usernames and balances.
#
# Example:
# alice - $500
# bob - $1200
#
#
# 2. CREATE ACCOUNT
# ------------------
# Ask the user for:
# - username
# - starting balance
#
# Add the account to the dictionary.
#
# If the username already exists:
# - print an error message
#
#
# 3. DEPOSIT MONEY
# -----------------
# Ask the user for:
# - username
# - deposit amount
#
# Add the money to the account balance.
#
# If the account does not exist:
# - print an error message
#
#
# 4. WITHDRAW MONEY
# ------------------
# Ask the user for:
# - username
# - withdrawal amount
#
# Requirements:
# - Check if the account exists
# - Check if there is enough money
#
# If successful:
# - subtract the money
#
#
# 5. TRANSFER MONEY
# ------------------
# Ask the user for:
# - sender username
# - receiver username
# - transfer amount
#
# Requirements:
# - Both accounts must exist
# - Sender must have enough money
#
# If successful:
# - subtract from sender
# - add to receiver
#
#
# 6. DELETE ACCOUNT
# ------------------
# Ask the user for a username.
#
# Remove the account from the dictionary.
#
# If the account does not exist:
# - print an error message
#
#
# 7. FIND RICHEST ACCOUNT
# ------------------------
# Find and print:
# - the username with the highest balance
# - their balance
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
# - Use functions for each menu option
# - Use a while loop for the menu
# - Use dictionary methods appropriately
# - Validate user input
# - Update balances correctly
#
#
# --------------------------------------------
# Initialize accounts dictionary
accounts = {}

def view_accounts():
    if not accounts:
        print("No accounts found.")
    else:
        for username, balance in accounts.items():
            print(f"{username} - ${balance}")

def create_account():
    username = input("Enter a username: ")
    if username in accounts:
        print("Error: Username already exists.")
        return
    try:
        starting_balance = float(input("Enter starting balance: "))
        if starting_balance < 0:
            print("Error: Starting balance cannot be negative.")
            return
    except ValueError:
        print("Error: Invalid input for balance.")
        return
    accounts[username] = starting_balance
    print(f"Account for {username} created with balance ${starting_balance}.")

def deposit_money():
    username = input("Enter username: ")
    if username not in accounts:
        print("Error: Account does not exist.")
        return
    try:
        deposit_amount = float(input("Enter deposit amount: "))
        if deposit_amount <= 0:
            print("Error: Deposit amount must be positive.")
            return
    except ValueError:
        print("Error: Invalid input for deposit amount.")
        return
    accounts[username] += deposit_amount
    print(f"${deposit_amount} deposited to {username}'s account. New balance: ${accounts[username]}.")

def withdraw_money():
    username = input("Enter username: ")
    if username not in accounts:
        print("Error: Account does not exist.")
        return
    try:
        withdrawal_amount = float(input("Enter withdrawal amount: "))
        if withdrawal_amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return
    except ValueError:
        print("Error: Invalid input for withdrawal amount.")
        return
    if accounts[username] < withdrawal_amount:
        print("Error: Insufficient funds.")
        return
    accounts[username] -= withdrawal_amount
    print(f"${withdrawal_amount} withdrawn from {username}'s account. New balance: ${accounts[username]}.")

def transfer_money():
    sender = input("Enter sender username: ")
    if sender not in accounts:
        print("Error: Sender account does not exist.")
        return
    receiver = input("Enter receiver username: ")
    if receiver not in accounts:
        print("Error: Receiver account does not exist.")
        return
    try:
        transfer_amount = float(input("Enter transfer amount: "))
        if transfer_amount <= 0:
            print("Error: Transfer amount must be positive.")
            return
    except ValueError:
        print("Error: Invalid input for transfer amount.")
        return
    if accounts[sender] < transfer_amount:
        print("Error: Insufficient funds in sender's account.")
        return
    accounts[sender] -= transfer_amount
    accounts[receiver] += transfer_amount
    print(f"${transfer_amount} transferred from {sender} to {receiver}.")

def delete_account():
    username = input("Enter username to delete: ")
    if username not in accounts:
        print("Error: Account does not exist.")
        return
    del accounts[username]
    print(f"Account for {username} has been deleted.")

def find_richest_account():
    if not accounts:
        print("No accounts found.")
        return
    richest_user = max(accounts, key=accounts.get)
    richest_balance = accounts[richest_user]
    print(f"The richest account is {richest_user} with a balance of ${richest_balance}.")

def main():
    while True:
        print("\nMenu Options:")
        print("1. View All Accounts")
        print("2. Create Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Delete Account")
        print("7. Find Richest Account")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            view_accounts()
        elif choice == '2':
            create_account()
        elif choice == '3':
            deposit_money()
        elif choice == '4':
            withdraw_money()
        elif choice == '5':
            transfer_money()
        elif choice == '6':
            delete_account()
        elif choice == '7':
            find_richest_account()
        elif choice == '8':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
    