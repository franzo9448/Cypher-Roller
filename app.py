#!/usr/bin/env python3
import os
import time
import sys
from platform import system
from termcolor import colored
from pyfiglet import Figlet
import pandas as pd
import random
from os import system
import logging
import fantasynames as names

# Excel file name
nome_file = "Cypher_roller.xlsx"

# Function to print exit options
def main_exit():
    print("  99 -- Exit")
    print("  999 - Back To Main Menu \n\n")
    choice = input("Neoikiru~# ")
    while choice not in ['99', '999']:
        print("Enter a valid value")
        choice = input("Neoikiru~# ")

    if choice == "99":
        neo_exit()
    elif choice == "999":
        main_menu()


# Function to print logo
def print_logo():
    text_logo = "Neoikiru"
    figlet = Figlet(font='slant')
    print(colored(figlet.renderText(text_logo), color="red"))

# Function to clear the screen
def clear_scr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Function to exit the program
def neo_exit():
    clear_scr()
    sys.exit()

# Function to get a random cypher type
def random_type():
    print_logo()
    df = pd.read_excel(nome_file, "Type")
    random_row = random.randint(1, 33)
    print((df.loc[random_row, "Types"]))

# Function to get a random cypher
def random_cypher():
    df = pd.read_excel(nome_file, "Cypher")
    pd.options.display.max_colwidth = 850
    random_row = random.randint(0, 20)
    columns = ["Name", "Level", "Description"]
    print(df.loc[random_row, columns])
    main_exit()

# Function to get a random minor artifact
def random_minor():
    print_logo()
    df = pd.read_excel(nome_file, "Minor Artifact")
    pd.options.display.max_colwidth = 850
    random_row = random.randint(1, 21)
    columns = ["Name", "Level", "Depletion","Effect"]
    print(df.loc[random_row, columns])
    main_exit()

# Function to get a random major artifact
def random_major():
    print_logo()
    df = pd.read_excel(nome_file, "Major Artifact")
    pd.options.display.max_colwidth = 850
    random_row = random.randint(1, 26)
    columns = ["Name", "Level", "Depletion", "Effect"]
    print(df.loc[random_row, columns])
    main_exit()

def main_menu():
    print_logo()
    menu_items = [
        ("Create random cypher", lambda: random_type() or random_cypher()),
        ("Create random minor artifact", random_minor),
        ("Create random major artifact", random_major),
        ("Fantasy names", names_menu),
        ("Dice roller", dice_menu),
        ("Bad Omens Generator", bad_omens),
        ("Random Encounters",encounters),
        ("Exit", neo_exit)
    ]
    menu_text = "\n".join(f"{i} -- {name}" for i, (name, _) in enumerate(menu_items, start=1))
    print(menu_text)
    choice = input("Neoikiru~# ")
    os.system('clear')
    try:
        item_index = int(choice) - 1
        item = menu_items[item_index]
        item[1]()
    except (ValueError, IndexError):
        main_menu()

def names_menu():
    print_logo()
    menu_text = (
        "1 -- Create random elf name\n"
        "2 -- Create random dwarf name\n"
        "3 -- Create random hobbit name\n"
        "4 -- Create random human name\n"
        "5 -- Create random anglo name\n"
        "6 -- Create random franco name\n"
        "99 - Return to main menù\n"
    )
    print(menu_text)

    while True:
        choice = input("Neoikiru~# ")
        if choice == "1":
            print(names.elf())
            break
        elif choice == "2":
            print(names.dwarf())
            break
        elif choice == "3":
            print(names.human())
            break
        elif choice == "4":
            print(names.hobbit())
            break
        elif choice == "5":
            print(names.anglo())
            break
        elif choice == "6":
            print(names.franco())
            break
        elif choice == "99":
            main_menu()
        else:
            print("Enter a valid choice.")

    print("\n\n1 -- Continue with names menu")
    print("99 -- Return to main menu")
    while True:
        choice = input("Neoikiru~# ")
        if choice == "1":
            names_menu()
            break
        elif choice == "99":
            main_menu()
        else:
            print("Enter a valid choice.")

def confirm_exit():
    while True:
        print("Do you want to return to the names menu or exit the program?")
        print("1 -- Return to names menu")
        print("2 -- Exit program")
        choice = input("Enter your choice: ")
        os.system('clear')
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                return False
            elif choice == 2:
                return True

def print_menu_options(options):
    for i, option in enumerate(options):
        print(f"{i+1} -- {option[0]}")
    print(f"{len(options)+1} -- Return to main menu")

def roll_dice(num_sides):
    result = random.randint(1, num_sides)
    print(f"You rolled a d{num_sides} and got {result}")
    choice = input("Enter 'c' to continue or 'm' to return to the main menu: ")
    while choice not in ['c', 'm']:
        print("Invalid choice. Please try again.")
        choice = input("Enter 'c' to continue or 'm' to return to the main menu: ")
    if choice == 'm':
        dice_menu()

def dice_menu():
    dice_dict = {
        1: 4,
        2: 6,
        3: 8,
        4: 10,
        5: 12,
        6: 20,
        7: 100
    }

    while True:
        print("Welcome to the Dice Roller! Please select a dice to roll:")
        for choice, num_sides in dice_dict.items():
            print(f"{choice}. d{num_sides}")
        print("8. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 8:
            main_menu()
        elif choice in dice_dict:
            result = roll_dice(dice_dict[choice])
            print(f"You rolled a d{dice_dict[choice]} and got {result}")
        else:
            print("Invalid choice. Please try again.")

def bad_omens():
    print_logo()
    bad_dict = {
        1: "A PC makes eye contact with a mysterious beggar, who gasps and runs away. If followed, they disappear.",
        2: "A raven caws angrily at the party before flying away. More are seen periodically, perching and watching.",
        3: "A woman in the street drops an urn, which shatters. There's a moment of silence in the street.",
        4: "A baby won't stop crying in a nearby basket. If the players investigate, there is no child. The crying is coming from the basket itself.",
        5: "The campfire goes out in the middle of the night. There is no wind. It is difficult to restart as darkness seems to loom around the players.",
        6: "The flames of nearby candles flicker out completely, but a moment later they return.",
        7: "The moon is larger and brighter than usual. It seems to dominate the sky, and cast harsh, pale shadows.",
        8: "A wooden road sign is snapped in half at a crossroads. It lies broken in the dirt.",
        9: "The clouds are gray and full of rain. And yet it does not rain. Though thunder rumbles, not a drop lands.",
        10: "A PC wakes up in the morning with a cut across their palm that wasn't there before.",
        11: "Animals go wild. Horses buck and have wide, scared eyes. Dogs bark fiercely and pull at their leashes.",
        12: "There's a large crack in a PC's drinking glass, and yet it doesn't break unless forced.",
        13: "A bird flies into the wall of a building and drops dead outside the door.",
        14: "A PC is contacted by the Sending spell, but they only hear heavy breathing and crying.",
        15: "The players hear distant, sourceless harp music. When pointed out or mentioned, it stops.",
        16: "An old man has a heart attack in the street. He stares directly at one of the PCs as he dies.",
        17: "A passed out drunk wakes suddenly and screams, clawing at his eyes. He runs and disappears.",
        18: "A strong wind that was blowing all day suddenly stops. The world is still for a few moments before life continues.",
        19: "A child chases an errant ball, only to trip and twist their ankle. The ball is not found.",
        20: "The temple doors are tossed open by a violent wind until a concerned acolyte rushes to close them.",
    }
    result = random.randint(1, 20)
    print(f"{result}. {bad_dict[result]}")
    main_exit()


def encounters():
    print_logo()
    # Genera un numero casuale tra 1 e 66 inclusi
    num = random.randint(1, 545)

    # Apre il file txt in modalità lettura
    with open('encounter.txt', 'r') as f:
        # Itera sulle righe del file
        lines = f.readlines()
        for line in lines:
            if str(num) in line:
                print(line.strip())
                break
    main_exit()

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    try:
        main_menu()
    except KeyboardInterrupt:
        print(" Finishing up...\r"),
        time.sleep(0.25)
