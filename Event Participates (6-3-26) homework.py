# ============================================
# Homework Assignment: Event Sign-Up System
# ============================================
#
# Objective:
# Practice using dictionaries and lists to
# manage event registrations.
#
# --------------------------------------------
# DATA STRUCTURE
# --------------------------------------------
#
# Example:
#
# events = {
#     "Basketball": ["Alice", "Bob"],
#     "Chess Club": ["Charlie"],
#     "Coding Workshop": []
# }
#
# Keys are event names.
# Values are lists of participants.
#
# --------------------------------------------
# MENU OPTIONS
# --------------------------------------------
#
# 1. View Events
# 2. Create Event
# 3. Register Participant
# 4. Remove Participant
# 5. Cancel Event
# 6. View Participants
# 7. Find Largest Event
# 8. Exit
#
# --------------------------------------------
# REQUIREMENTS
# --------------------------------------------
#
# 1. VIEW EVENTS
# ---------------
# Display all events and the number of
# participants registered.
#
#
# 2. CREATE EVENT
# ----------------
# Ask for an event name.
#
# Create a new event with no participants.
#
# If the event already exists:
# - print an error message
#
#
# 3. REGISTER PARTICIPANT
# ------------------------
# Ask for:
# - event name
# - participant name
#
# Add the participant to the event.
#
# Requirements:
# - Event must exist
# - Participant cannot already be registered
#
#
# 4. REMOVE PARTICIPANT
# ----------------------
# Ask for:
# - event name
# - participant name
#
# Remove the participant from the event.
#
#
# 5. CANCEL EVENT
# ----------------
# Delete an event and all registrations.
#
#
# 6. VIEW PARTICIPANTS
# ---------------------
# Ask for an event name and display all
# registered participants.
#
#
# 7. FIND LARGEST EVENT
# ----------------------
# Find and print:
# - event name
# - number of participants
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
# - Use lists as dictionary values
# - Validate user input
#
# --------------------------------------------
# START CODING BELOW
# --------------------------------------------
events = {}
event_name = ""
def view_events(events):
    if not events:
        print("No events available.")
    else:
        print("Events:")
        for event, participants in events.items():
            print(f"{event} - {len(participants)} participants")
def create_event(events):
    event_name = input("Enter the name of the event: ")
    if event_name in events:
        print("Event already exists.")
    else:
        events[event_name] = []
        print(f"Event '{event_name}' created.")
def register_participant(events):
    event_name = input("Enter the name of the event: ")
    if event_name not in events:
        print("Event does not exist.")
        return
    
    participant_name = input("Enter the name of the participant: ")
    if participant_name in events[event_name]:
        print("Participant already registered.")
    else:
        events[event_name].append(participant_name)
        print(f"Participant '{participant_name}' registered for '{event_name}'.")
def remove_participant(events):
    event_name = input("Enter the name of the event: ")
    if event_name not in events:
        print("Event does not exist.")
        return
    participant_name = input("Enter the name of the participant: ")
    if participant_name in events[event_name]:
        events[event_name].remove(participant_name)
        print(f"Participant '{participant_name}' removed from '{event_name}'.")
    else:
        print("Not Found")
def cancel_event(events):
    event_name = input("Enter the name of the event to cancel: ")
    if event_name in events:
        del events[event_name]
        print(f"Event '{event_name}' has been canceled.")
    else:
        print("Event does not exist.")
def view_participants(events):
    event_name = input("Enter the name of the event: ")
    if event_name in events:
        participants = events[event_name]
        if participants:
            print(f"Participants in '{event_name}':")
            for participant in participants:
                print(participant)
        else:
            print(f"No participants registered for '{event_name}'.")
    else:
        print("Event does not exist.")
def find_largest_event(events):
    if not events:
        print("No events available.")
        return

    largest_event = max(events, key=lambda e: len(events[e]))
    num_participants = len(events[largest_event])
    print(f"Largest event: '{largest_event}' with {num_participants} participants.")
def main():
    events = {}
    
    while True:
        print("\nEvent Sign-Up System")
        print("1. View Events")
        print("2. Create Event")
        print("3. Register Participant")
        print("4. Remove Participant")
        print("5. Cancel Event")
        print("6. View Participants")
        print("7. Find Largest Event")
        print("8. Exit")
        
        choice = input("Select an option (1-8): ")
        
        if choice == '1':
            view_events(events)
        elif choice == '2':
            create_event(events)
        elif choice == '3':
            register_participant(events)
        elif choice == '4':
            remove_participant(events)
        elif choice == '5':
            cancel_event(events)
        elif choice == '6':
            view_participants(events)
        elif choice == '7':
            find_largest_event(events)
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()

        
