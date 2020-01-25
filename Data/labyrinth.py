from random import randint

import pygame
from pygame.locals import *
import Data.constants as constants


class Labyrinth:

    """
    This class is to initialize the game board
    from the file "structure" wich contains the structure of the labyrinth,
    and chose ramdomly a free space on the structure
    """

    def __init__(self):

        # Read the file "structure" and save the structure of the labyrinth
        # as a list in structure []
        # With open == open file and auto-close
        with open("Data/draw_file", 'r') as labyrinth: # ,"r" == open for reading, no writing
           
            """
            Optimized according to Gérard Swinnen's book. This replaces 2 for loops
            
            for line in labyrinth to create a list of lines
            for letter in line to create a list of letters (ignoring end of line characters)
            """
            self.structure = [[letter for letter in line if letter != "\n"] for line in labyrinth]


    def place_object_in_maze(self):
        """
        Find a random free position to place the items in the maze
        """
        random_line = randint(0, len(self.structure) -1)
        random_tile = randint(0, len(self.structure[random_line]) -1)
        place_object_in_maze = self.structure[random_line][random_tile]
        while place_object_in_maze != " ":
            random_tile = randint(0, len(self.structure[random_line]) -1)
            place_object_in_maze = self.structure[random_line][random_tile]
        return random_line, random_tile

    def character_position(self, chara_letter):
        """
        Find the Departure tile to place Macgyver and Finish tile to place Guardian
        """           
        for y, line in enumerate(self.structure):
            for x, letter in enumerate(line):
                if self.structure[y][x] == chara_letter:
                    position = y, x
                    return position

    def lab_display(self, window):
        """
        This method loads the images from "constants" and place them on structure
        """
        
        wall = pygame.image.load(constants.WALL_IMG).convert_alpha()
        departure = pygame.image.load(constants.departure_img).convert_alpha()
        needle = pygame.image.load(constants.needle_img).convert_alpha()
        alcohol = pygame.image.load(constants.alcohol_img).convert_alpha()
        guardian = pygame.image.load(constants.guardian_img).convert_alpha()
        toilet_tube = pygame.image.load(constants.toilet_tube_img).convert_alpha()        
        line = 0
        for ligne in self.structure:
            case = 0
            for sprite in ligne:
                y = case * constants.sprite_size
                x = line * constants.sprite_size
                if sprite == 'w':
                    window.blit(wall, (y, x))
                elif sprite == 'D':
                    window.blit(departure, (y, x))
                elif sprite == 'N':
                    window.blit(needle, (y, x))
                elif sprite == 'A':
                    window.blit(alcohol, (y, x))
                elif sprite == "G":
                    window.blit(guardian, (y, x))
                elif sprite == 'T':
                    window.blit(toilet_tube, (y, x))
                case += 1
            line += 1
