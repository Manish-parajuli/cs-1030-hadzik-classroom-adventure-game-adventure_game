import sys

# Player class with health and inventory tracking
class Player:
    def __init__(self):
        self.health = 100
        self.inventory = []

# Helper Functions
def stay_still(player):
    print("\nYou decide to stay still. Time passes...")
    player.health -= 10
    print("You feel weaker from doing nothing (-10 health).")

def check_win(player):
    if "treasure" in player.inventory and "rare herbs" in player.inventory:
        print("\n🎉 You have found the treasure and the rare herbs!")
        print("🏆 You win! Congratulations, brave adventurer!")
        sys.exit()

def check_lose(player):
    if player.health <= 0:
        print("\n💀 You have lost all your health.")
        print("Game over.")
        sys.exit()

def show_status(player):
    print(f"\n❤️ Health: {player.health}")
    print(f"🎒 Inventory: {player.inventory}")

# Area Functions
def explore_dark_woods(player):
    print("\nYou venture into the dark woods.")
    print("You find a lantern hanging from a tree!")
    if "lantern" not in player.inventory:
        player.inventory.append("lantern")
        print("You take the lantern.")

def explore_mountain_pass(player):
    print("\nYou carefully climb the mountain pass.")
    print("You find an old map buried under some rocks!")
    if "map" not in player.inventory:
        player.inventory.append("map")
        print("You take the map.")

def explore_cave(player):
    print("\nYou enter the dark cave...")
    if "lantern" not in player.inventory:
        print("It's too dark! You stumble and hurt yourself.")
        player.health -= 10
    else:
        if "treasure" not in player.inventory:
            print("With your lantern, you discover a treasure chest!")
            player.inventory.append("treasure")
            print("You collect the treasure.")
        else:
            print("You’ve already collected the treasure.")

def explore_hidden_valley(player):
    print("\nYou try to find the hidden valley...")
    if "map" not in player.inventory:
        print("You get lost and exhaust yourself in the wild.")
        player.health -= 10
    else:
        if "rare herbs" not in player.inventory:
            print("Guided by your map, you find the rare healing herbs!")
            player.inventory.append("rare herbs")
            print("You collect the herbs.")
        else:
            print("You’ve already collected the rare herbs.")

# Main Game Loop
def main():
    player = Player()
    print("🌲 Welcome to the Final Adventure Game!")
    print("Your goal is to collect the treasure and the rare herbs.")
    
    while True:
        show_status(player)
        print("\nWhere would you like to go?")
        print("1. Dark Woods")
        print("2. Mountain Pass")
        print("3. Cave")
        print("4. Hidden Valley")
        print("5. Stay Still")
        print("6. Quit")
        
        choice = input("Choose an action (1-6): ")
        
        if choice == "1":
            explore_dark_woods(player)
        elif choice == "2":
            explore_mountain_pass(player)
        elif choice == "3":
            explore_cave(player)
        elif choice == "4":
            explore_hidden_valley(player)
        elif choice == "5":
            stay_still(player)
        elif choice == "6":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Choose again.")

        check_win(player)
        check_lose(player)

if __name__ == "__main__":
    main()
