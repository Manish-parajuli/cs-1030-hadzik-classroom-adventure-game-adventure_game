'''
DOCSTRING
Adventure Game
Author: Scott Hadzik
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''

#------------------------
# Player class to store player info and game state
#------------------------
class Player:
    # initializer - constructor
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False

# TODO:  Add a check before certain choices
#       - Change 
#           - 3. Stay where you are. 
#           to
#           - 4. Stay where you are.
#       - Create a new option  
#           - 3. Enter the Cave 
#       - Update 
#           - You see two paths ahead:
#           - There are multiple paths ahead:
#       - If player.has_lantern is False, prevent entering a cave
#       - Print a message  
#           - “It’s too dark to continue without a lantern.”

#----------------
# Function: welcome_player
# Greets the player, asks for their name,
# and returns the name as a string
#----------------
def welcome_player():
    # Welcome message and introduction
    print("Welcome to the Adventure Game!")  
    print('Your journey begins here... ')

    # Ask for the player's name
    name = input("What is your name, adventurer? ")
    player = Player(name)

    # Use an f-string to display the same message in a more readable way
    print(f"Welcome, {player.name}! Your journey begins now.")

    return player

#----------------
# Function: describe_area
# Print the opening description of the area
#----------------
def describe_area():
    # Describe the starting area
    print( """
    You find yourself in a dark forest
    The sound of rustling leaves fills the air
    A faint path lies ahead, leading deeper into the
    unknown... """)

#----------------
# Function: add_to_inventory
# Accepts an item name as a parameter,
# adds it to the inventory list,
# and confirm the pickup to the player
#----------------
def add_to_inventory(item):
    player.inventory.append(item)
    print(f"You picked up a {item}!")

#-----------------
# Game starts here
# Call the welcome and describe area functions
#-----------------

player = welcome_player()
describe_area()

#-----------------
# Main game loop
# run this until the player quiescent
#-----------------

# Start the game Loop
while True:
    print("\nYou see two paths ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Stay where you are.")
    print("\tType 'i' to view your inventory.")

    decision = input("What will you do (1,2,3 or i): ").lower()

    if decision == 'i':
        print("Inventory", player.inventory)
        continue

    if decision == "1":
        print(f"{player.name}, you step into the dark woods."
              "The trees whisper as walk deeper.")
        add_to_inventory("lantern")
        player.has_lantern = True

    elif decision == "2":
        print(f"{player.name}, you make your way "
              "towards the mountain pass, feeling "
              "the cold wind against your face.")
        add_to_inventory("map")
        player.has_map = True
        
    elif decision == "3":
        print("You stay still, listening to the " 
              "distant sounds of the forest")
    else: 
        print("Invalid choice. Please choose "
              "1, 2, or 3.")
    
    # Ask if they want to continue
    play_again = input("Do you want to continue "
                       "exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player.name} "
              "See you next time.")
        break # Exit the loop and end the game
    
