import random

# Dictionary to store scene descriptions and options
scenes = {
    "crossroads": {
        "description": "You are at a crossroads. You can see paths leading left, right, and forward.",
        "options": {
            "left": "darkTunnel",
            "right": "hiddenDoor",
            "forward": "skeletonChamber"
        }
    },
    "darkTunnel": {
        "description": "You enter a dark tunnel. You can barely see anything. Suddenly, you hear footsteps approaching.",
        "options": {
            "hide": "crossroads",
            "confront": "crossroads"
        }
    },
    "hiddenDoor": {
        "description": "You discover a hidden door. There seems to be some faint light coming from inside.",
        "options": {
            "enter": "treasureRoom",
            "continue": "crossroads"
        }
    },
    "skeletonChamber": {
        "description": "You enter a chamber filled with skeletons. There's a sense of unease in the air.",
        "options": {
            "investigate": "treasureRoom",
            "leave": "crossroads"
        }
    },
    "treasureRoom": {
        "description": "You enter a room filled with treasure! Gold coins, precious gems, and valuable artifacts sparkle in the dim light.",
        "options": {
            "celebrate": "celebrate",
            "take": "takeTreasure"
        }
    }
}

def introScene():
    print("Welcome to the Adventure Game!")
    print("As an avid traveler, you have decided to visit the Catacombs of Paris.")
    print("However, during your exploration, you find yourself lost.")
    name = input("Let's start with your name: ")
    print("Good luck, " + name + ".")

def displayScene(scene_name):
    print(scenes[scene_name]["description"])
    return scene_name

def handleOptions(scene_name):
    options = scenes[scene_name]["options"]
    while True:
        print("Choose your action:")
        for option, next_scene in options.items():
            print(f"- {option}")
        choice = input("What will you do? ").lower()
        if choice in options:
            return options[choice]
        else:
            print("Invalid choice. Try again.")

def celebrate():
    print("You take a moment to revel in your success.")

def takeTreasure():
    print("You carefully gather some treasure to take with you.")

def playGame():
    introScene()
    current_scene = "crossroads"
    while True:
        current_scene = displayScene(current_scene)
        next_scene = handleOptions(current_scene)
        if next_scene == "celebrate":
            celebrate()
            break
        elif next_scene == "take":
            takeTreasure()
            break
        current_scene = next_scene

if __name__ == "__main__":
    playGame()
