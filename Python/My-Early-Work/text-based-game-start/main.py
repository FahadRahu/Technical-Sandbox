# Print the Title of the Game
import sys
import string
import textwrap
import time


def main_menu():
    print("***Welcome to the Journey to Mount Qaf", end="\n\n")
    # Print the Main Menu Options
    print("1. Start a new game (START)", "2. Load your progress (LOAD)", "3. Quit the game (QUIT)", sep="\n")
    # User Selects their Main Menu Option
    while True:
        main_option = input()
        if main_option in ["1", "start"]:
            print("Starting a new game...")
            return "start"
        elif main_option in ["2", "load"]:
            print("No saved data found")
            return "load"
        elif main_option in ["3", "quit"]:
            print("Goodbye!")
            return "quit"
        else:
            print("Unknown input! Please enter a valid one.")


def start_new():
    global usernames_dict
    while True:
        username = input("Enter a username ('/b') to go back: ")
        if username.lower() == "/b":
            return None
        else:
            user_count = len(usernames_dict) + 1
            return username, user_count


def create_character():
    print("Create your character:")
    name = input("\tName: ")
    species = input("\tSpecies: ")
    gender = input("\tGender: ")
    return name, species, gender


def create_bag():
    print("Pack your bag for the journey:")
    snack = input("\tSnack: ")
    weapon = input("\tWeapon: ")
    tool = input("\tTool: ")
    return snack, weapon, tool


def create_difficulty():
    print("Choose your difficulty:")
    print("\t1. Easy", "2. Medium", "3. Hard", sep="\n\t")
    while True:
        difficulty = input()
        if difficulty.lower() not in ['easy', 'medium', 'hard', '1', '2', '3']:
            print("Unknown input! Please enter a valid one.")
            continue
        else:
            difficulty = difficulty.lower()
            if difficulty in ["easy", "1"]:
                difficulty = "easy"
                lives = 5
            elif difficulty in ["medium", "2"]:
                difficulty = "medium"
                lives = 3
            elif difficulty in ["hard", "3"]:
                difficulty = "hard"
                lives = 1
            else:
                difficulty = "none"
                lives = 99
            break
    return difficulty, lives


def game_stats(username, name, species, gender, snack, weapon, tool, difficulty, lives):
    print(f"Good luck on your journey, {username}!")
    print(f"Your character: {name}, {species}, {gender}")
    print(f"Your inventory: {snack}, {weapon}, {tool}")
    print(f"Difficulty: {difficulty}")
    print(f"Number of lives: {lives}")


usernames_dict = {}

while True:
    main_menu_option = main_menu()
    if main_menu_option == "start":
        start_time = time.time()
        while True:
            user_details = start_new()
            if user_details is None:
                main_menu()
            else:
                username, user_count = user_details
                name, species, gender = create_character()
                snack, weapon, tool = create_bag()
                difficulty, lives = create_difficulty()
                game_stats(username, name, species, gender, snack, weapon, tool, difficulty, lives)
                break
        break
    elif main_menu_option == "load":
        pass
    elif main_menu_option == "quit":
        print("Double Goodbye!")
