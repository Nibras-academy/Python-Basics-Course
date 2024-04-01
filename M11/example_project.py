import random

# Define initial player attributes
player = {
    "name": "",
    "health": 100,
    "hunger": 50,
    "thirst": 50,
    "shelter": False,
    "friends": []
}

# Define lists for resources and events
resources = ["food", "water", "wood", "stone"]
events = ["encounter wild animal", "find hidden treasure", "meet another castaway"]

# Function to initialize the game
def start_game():
    print("Welcome to Stranded Island Adventure!")
    player["name"] = input("What is your name? ")
    print(f"Hello, {player['name']}! Your ship has crashed, and you find yourself stranded on a deserted island.")
    print("Your goal is to survive and find a way to escape before it's too late.")

# Function to display player status
def display_status():
    print(f"\nStatus: Health - {player['health']} | Hunger - {player['hunger']} | Thirst - {player['thirst']}")
    print("Resources:", resources)
    print("Events:", events)

# Function to handle player actions
def player_action():
    action = input("\nWhat would you like to do? (explore/gather/build/rest/quit): ").lower()
    if action == "explore":
        explore()
    elif action == "gather":
        gather()
    elif action == "build":
        build()
    elif action == "rest":
        rest()
    elif action == "quit":
        print("Thanks for playing! Goodbye.")
        exit()
    else:
        print("Invalid action. Please try again.")
        player_action()

# Function to simulate exploring the island
def explore():
    event = random.choice(events)
    print(f"You are exploring the island and {event}.")
    if event == "encounter wild animal":
        print("Oh no! You encountered a wild animal.")
        print("Your health decreases by 20.")
        player["health"] -= 20
    elif event == "find hidden treasure":
        print("You found a hidden treasure!")
        resources.append("treasure")
    elif event == "meet another castaway":
        print("You found another castaway!")
        player["friends"].append("Another Castaway")

# Function to gather resources
def gather():
    resource = random.choice(resources)
    print(f"You are gathering {resource}.")
    resources.append(resource)

# Function to build shelter
def build():
    if "wood" in resources and "stone" in resources:
        print("You build a shelter.")
        player["shelter"] = True
        resources.remove("wood")
        resources.remove("stone")
    else:
        print("You don't have enough resources to build a shelter.")

# Function to rest and regain health
def rest():
    print("You take some rest.")
    player["health"] += 10

# Main game loop
def play_game():
    start_game()
    while True:
        display_status()
        player_action()

# Start the game
if __name__ == "__main__":
    play_game()




