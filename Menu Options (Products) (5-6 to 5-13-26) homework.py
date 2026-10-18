# --------------------------------------------
# MENU OPTIONS
# --------------------------------------------
#
# 1. View Inventory
# 2. Add Product
# 3. Restock Product
# 4. Purchase Product
# 5. Remove Product
# 6. Exit
#
# The program should continuously run in a
# while loop until the user chooses Exit.
#
# --------------------------------------------
# REQUIREMENTS
# --------------------------------------------
#
# 1. VIEW INVENTORY
# -----------------
# Display all products in the inventory.
#
# Example Output:
# apple - $1.50 (Stock: 10)
#
#
# 2. ADD PRODUCT
# ---------------
# Ask the user for:
# - product name
# - price
# - stock amount
#
# Add the product to the inventory dictionary.
#
# If the product already exists:
# - print an error message
#
#
# 3. RESTOCK PRODUCT
# -------------------
# Ask the user:
# - product name
# - amount to add
#
# Increase the product's stock.
#
# If the product does not exist:
# - print an error message
#
#
# 4. PURCHASE PRODUCT
# --------------------
# Ask the user:
# - product name
# - quantity to purchase
#
# Requirements:
# - Check if the product exists
# - Check if enough stock is available
#
# If purchase is successful:
# - subtract stock
# - calculate total price
# - print total cost
#
# Example:
# Total: $4.50
#
#
# 5. REMOVE PRODUCT
# ------------------
# Ask the user for a product name.
#
# Remove the product from the inventory.
#
# If product does not exist:
# - print an error message
#
#
# 6. EXIT
# --------
# End the program.
print("Welcome to the Inventory!")
print(" 1. View Inventory")
# inventory = {key - name: value - { price: $1 , stock: 10 } }
print(" 2. Add Product")
print(" 3. Restock Product") # user inputs product name and stock -> increasing inventory's values with user inputted stock value
print(" 4. Purchase Product") # user inputs product name and stock  -> decreasing inventory's values with user inputted stock value
print(" 5. Remove Product") # user inputs product name -> completely remove product from the inventory 
print(" 6. Exit")
inventory = {}
ask_product = ""
while ask_product != "6":
    ask_product = input("What would you like to do? ")
    if ask_product == "1":
        for product in inventory:
            print(f"{product} - ${inventory[product]['price']} (Stock: {inventory[product]['stock']})")
    elif ask_product == "2":
        add_product = input("What product would you like to add? ")
        if add_product in inventory:
            print("Product already exists!")
            continue
        add_price = float(input("What is the price of the product? "))
        add_stock = int(input("How much stock does the product have? "))
        inventory[add_product] = {"price": add_price, "stock": add_stock}
    elif ask_product == "3":
        restock_product = input("What product would you like to restock? ")
        if restock_product not in inventory:
            print("Product does not exist!")
            continue
        restock_amount = int(input("How much stock would you like to add? "))
        inventory[restock_product]["stock"] += restock_amount
    elif ask_product == "4":
        purchase_product = input("What product would you like to purchase? ")
        if purchase_product not in inventory:
            print("Product does not exist!")
            continue
        purchase_quantity = int(input("How many would you like to purchase? "))
        if purchase_quantity > inventory[purchase_product]["stock"]:
            print("Not enough stock available!")
            continue
        inventory[purchase_product]["stock"] -= purchase_quantity
        total_cost = purchase_quantity * inventory[purchase_product]["price"]
        print(f"Total: ${total_cost:.2f}")
    elif ask_product == "5":
        remove_product = input("What product would you like to remove? ")
        if remove_product not in inventory:
            print("Product does not exist!")
            continue
        del inventory[remove_product]
    elif ask_product == "6":
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid option. Please choose a number from 1 to 6.")
