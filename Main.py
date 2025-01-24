# This is the File that runs the game and puts all the pieces together

# TODO: Difficulty - Easy, Medium, Hard
# TODO: Oregon Trail - Goal is to make it back to Earth

# Imports
import json
import sys
from time import sleep
from Classes.Ship import Ship
from Classes.Player import Player
from Classes.Game import Game
from Classes.Map import Map


def main_menu() -> None:
    """Plays the main menu"""
    # TODO: Test this and rework
    option = 'woah'
    while option.lower() != 'play':
        print("\n")
        print("#####################################")
        print("#####################################")
        print("#     WELCOME TO SPACE ADVENTURE    #")
        print("#####################################")
        print("#####################################")
        print("#             -Play-                #")
        print("#             -Info-                #")
        print("#             -Quit-                #")
        print("#####################################")
        print("\n")

        option = input("Choose an option> ")
        if option.lower() == "play":
            play = "lets get started!~"
            for i in play:
                sleep(.3)
                print(i)
            return
        elif option.lower() == "info":
            info()
        elif option.lower() == "quit":
            print("\n")
            print("#####################################")
            print("#####################################")
            bye = "             BYE FELICIA             " + "\n"
            for i in bye:
                sleep(.1)
                sys.stdout.write(i)
                sys.stdout.flush()
            print("#####################################")
            print("#####################################")
            sys.exit()


def info() -> None:
    """Information about the game"""
    print("\n")
    print("This game was created by Thomas Eavns")
    print("Copyright 2025. All rights reserved")
    return


def load_json_files() -> None:
    """Loads the json files for the game"""
    # TODO: Return as a tuple

        # Loads Ship json file
    with open('./Json Files/ships.json', 'r') as file:
        ship_data = json.load(file)
    # Loads factions json file
    # TODO: Load factions

    # Loads Planet json file
    with open('./Json Files/planet.json', 'r') as file:
        planet_data = json.load(file)

    # Load Statement json file
    with open('./Json Files/statements.json', 'r') as file:
        statements_data = json.load(file)
    return (ship_data, planet_data, statements_data)


# use cmd
if __name__ == '__main__':

    ###############################################################################
    # Load game Json files
    ###############################################################################
    main_menu()

    with open('./Json Files/ships.json', 'r') as file:
        ship_data = json.load(file)

    # TODO: while loop that starts up game and keeps game running

    ############################################################################
    # Initializers
    ############################################################################
    
    #map = Map()

# initialize Player
    player = Player()
    print(player)

    ship = ship_data['Class']['Sub']
    data = Ship('Class', 'Sub', **ship_data['Class']['Sub'])

    game = Game().non_combat_mode(data, player)

    # initialize Game

    # # TODO: look into this some more
    # # TODO: Pass the ship_data as a **kwarg
    
    # print(ship)

    
    # data2 = Ship('Class', 'Sub', **ship_data['Class']['Sub'])
    # print(data)
    # print(data2)`
