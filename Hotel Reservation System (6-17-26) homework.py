# ============================================
# Homework Assignment: Hotel Reservation System
# ============================================
#
# Objective:
# Practice using dictionaries and lists to
# manage hotel rooms and reservations.
#
# --------------------------------------------
# DATA STRUCTURE
# --------------------------------------------
#
# Example:
#
# rooms = {
#     101: "Available",
#     102: "Occupied",
#     103: "Available"
# }
#
# reservations = [
#     {"guest": "Alice", "room": 102}
# ]
#
# The rooms dictionary stores room statuses.
# The reservations list stores guest bookings.
#
# --------------------------------------------
# MENU OPTIONS
# --------------------------------------------
#
# 1. View Rooms
# 2. Book Room
# 3. Check Out
# 4. View Reservations
# 5. Add Room
# 6. Remove Room
# 7. Find Occupied Rooms
# 8. Exit
#
# --------------------------------------------
# REQUIREMENTS
# --------------------------------------------
#
# 1. VIEW ROOMS
# --------------
# Display all rooms and their status.
#
# Example:
# Room 101 - Available
# Room 102 - Occupied
#
#
# 2. BOOK ROOM
# -------------
# Ask for:
# - guest name
# - room number
#
# Requirements:
# - room must exist
# - room must be available
#
# If successful:
# - mark the room as occupied
# - add a reservation
#
#
# 3. CHECK OUT
# -------------
# Ask for:
# - room number
#
# Requirements:
# - room must exist
# - room must be occupied
#
# If successful:
# - mark the room as available
# - remove the reservation
#
#
# 4. VIEW RESERVATIONS
# ---------------------
# Display all reservations.
#
# Example:
# Alice - Room 102
# Bob - Room 104
#
#
# 5. ADD ROOM
# ------------
# Ask for:
# - room number
#
# Add a new available room.
#
# If the room already exists:
# - print an error message
#
#
# 6. REMOVE ROOM
# ---------------
# Ask for:
# - room number
#
# Requirements:
# - room must exist
# - room cannot be occupied
#
# Remove the room from the hotel.
#
#
# 7. FIND OCCUPIED ROOMS
# -----------------------
# Display all rooms that are currently
# occupied.
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
# - Use a dictionary
# - Use a list
# - Validate user input
# - Keep room statuses and reservations
#   synchronized

rooms = {}

reservations = []
def view_rooms():
    print("\nRoom Statuses:")
    for room, status in rooms.items():
        print(f"Room {room} - {status}")
def book_room(): 
    guest_name = input("Enter guest name: ")
    try:
        room_number = int(input("Enter room number to book: "))
    except ValueError:
        print("Invalid room number. Please enter a valid integer.")
        return

    if room_number not in rooms:
        print("Error: Room does not exist.")
        return
    if rooms[room_number] == "Occupied":
        print("Error: Room is already occupied.")
        return

    rooms[room_number] = "Occupied"
    reservations.append({"guest": guest_name, "room": room_number})
    print(f"Room {room_number} successfully booked for {guest_name}.")
def check_out():
    try:
        room_number = int(input("Enter room number to check out: "))
    except ValueError:
        print("Invalid room number. Please enter a valid integer.")
        return

    if room_number not in rooms:
        print("Error: Room does not exist.")
        return
    if rooms[room_number] == "Available":
        print("Error: Room is not currently occupied.")
        return

    rooms[room_number] = "Available"
    reservations[:] = [res for res in reservations if res["room"] != room_number]
    for res in reservations:
        if res["room"] == room_number:
            reservations.remove(res)
            break
    

    print(f"Room {room_number} has been checked out and is now available.")
def view_reservations():
    if not reservations:
        print("No reservations found.")
    else:
        print("\nCurrent Reservations:")
        for res in reservations:
            print(f"{res['guest']} - Room {res['room']}")
def add_room():
    try:
        room_number = int(input("Enter new room number to add: "))
    except ValueError:
        print("Invalid room number. Please enter a valid integer.")
        return

    if room_number in rooms:
        print("Error: Room already exists.")
        return

    rooms[room_number] = "Available"
    print(f"Room {room_number} has been added and is now available.")
def remove_room():
    try:
        room_number = int(input("Enter room number to remove: "))
    except ValueError:
        print("Invalid room number. Please enter a valid integer.")
        return

    if room_number not in rooms:
        print("Error: Room does not exist.")
        return
    if rooms[room_number] == "Occupied":
        print("Error: Cannot remove an occupied room.")
        return

    del rooms[room_number]
    print(f"Room {room_number} has been removed from the hotel.")
def find_occupied_rooms():
    occupied_rooms = [room for room, status in rooms.items() if status == "Occupied"]

        # for room, status in rooms.items():
        #     if status == "Occupied":
        #         occupied_rooms.append(room)
    
    if not occupied_rooms:
        print("No rooms are currently occupied.")
    else:
        print("\nOccupied Rooms:")
        for room in occupied_rooms:
            print(f"Room {room}")
def display_menu():
    while True:
        print("\nHotel Reservation System Menu:")
        print("1. View Rooms")
        print("2. Book Room")
        print("3. Check Out")
        print("4. View Reservations")
        print("5. Add Room")
        print("6. Remove Room")
        print("7. Find Occupied Rooms")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            view_rooms()
        elif choice == "2":
            book_room()
        elif choice == "3":
            check_out()
        elif choice == "4":
            view_reservations()
        elif choice == "5":
            add_room()
        elif choice == "6":
            remove_room()
        elif choice == "7":
            find_occupied_rooms()
        elif choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    display_menu()