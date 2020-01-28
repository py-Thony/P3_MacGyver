#!/usr/bin/python3
# -*- coding: Utf-8 -*-

"""
The PEP8 convention: 
The standard Python library is conservative and requires limiting lines 
to 79 characters (and docstrings or comments to 72).
I therefore put the line using ' \ ' to respect this convention.
|-------------------------Max width of comments------------------------|
|-------------------------Max width of the code-------------------------------|

Limiting the required editor window width allows you to open multiple 
files side-by-side and works well when you use code review tools that 
present both versions in adjacent columns.


The use of docstrings can be described as abusive, but I remind you 
that this is to demonstrate a complete understanding of the code .
The choice of docstring instead of multi-line comments is only a 
question of readability of the code overloaded with annotations.
"""

# Module to use random function
from random import randint

# Module for use 2D graphics
import pygame

# Submodules of Pygame
from pygame.locals import *

"""
Importing only what is necessary reduces the loading in memory.
The second advantage resides in the fact of knowing the state of each 
variable (via pylint in VScode) when the code is updated.

And obliging to an additional rigor concerning the control of code.
"""
from Data.constants import WALL_IMG, DEPARTURE_IMG, NEEDLE_IMG, ALCOHOL_IMG, \
                           GUARDIAN_IMG, TOILET_TUBE_IMG, SPRITE_SIDE_SIZE, \
                           DRAW_FILE

"""
To comply with the naming PEP8 convention:
            
            - variable == VARIABLE
              (all in capital letters)
            
            - method, function == method, function
              (all lowercase)
            
            - class, classclass == Class, ClassClass
              (first letter of words in uppercase)
            
            - 1var is forbidden, var1 allowed
              (a name must start with a letter)
            
            - myVarOne accepted but my_var_one recommannded  
              (the naming can be adapted but must remain consistent)
            
            - all characters except '_' are prohibited
              (@, !, #, ... prohibited)
            
            - acronym in CapWord allways in uppercase
              (HTTPServerError: yes, HttpServerError: no!)
"""

class Labyrinth:

    """
    This class is to initialize the game board
    from the file "structure" wich contains the structure of the 
    labyrinth,and choose ramdomly a free space on the structure
    """

    def __init__(self):

        """
        Read the file "structure" 
        and save the structure of the 'draw_file'
        as a list in structure []
        
        With open == open file and auto-close
        "r" == open for reading, no writing
        """
        with open(DRAW_FILE, 'r') as labyrinth:
            
            """
            Optimized according to Gérard Swinnen's book. 
            This replaces 2 for loops
            
            - for line in labyrinth to create a list of lines
            - for letter in line to create a list of letters 
              (ignoring end of line characters)
            """
            # Demo of understanding the cutting of code line too long
            self.structure = [
                [letter for letter in line if letter != "\n"] 
                for line in labyrinth
            ]


    def character_position(self, chara_letter):
        """
        Find the Departure tile to place Macgyver and Finish tile 
        to place Guardian
        """
        # List each line         
        for y, line in enumerate(self.structure):
            # List each letter in each line
            for x, letter in enumerate(line):
                # Find the letter you are looking for
                if self.structure[y][x] == chara_letter:
                    # Determine the position of the letter
                    position = y, x
                    # return the position of the letter
                    return position

    def item(self, name, structure, position):
        """
        Defines the general rule of creation, recognition, 
        positioning of each item according to its letter 

        (Read in 'DRAW_FILE' and granted according to 
        the first letter of the item in capital letters)
        """
        # The name of item in 'lab_display'
        self.name = name
        # The position in lab.structure
        self.position = position
        # The structure of labyrinth
        self.structure = structure
        # Position define by reading of the list structure
        self.case_y = position[0]
        self.case_x = position[1]
        # According first letter of item with position of structure
        self.structure[self.case_y][self.case_x] = name[0]
        return position

    def place_objects_in_maze(self):

        """
        Random positioning, provided that the location is an empty box.
        If the box is not empty, the search is restarted.
        """

        # -1 == width of the labyrinth minus 1 box 
        # (We count from zero, so we would have a calculation 
        # on 16 boxes instead of 15)
        random_line = randint(0, len(self.structure) -1)
        random_tile = randint(0, len(self.structure[random_line]) -1)
        

        """
        When working with list of lists, we need to refer to 
        multiple index numbers in order to access specific items 
        in the appropriate nested list.
        """
        place_object_in_maze = self.structure[random_line][random_tile]
        
        # As long as the condition is verified
        while place_object_in_maze != " ":
            
            # Random empty box for a line of structure (list)
            random_tile = randint(0, len(self.structure[random_line]) -1)
            # Choose a random tile in a random list of lines
            place_object_in_maze = self.structure[random_line][random_tile]
        
        # Return random position of random tile
        return random_line, random_tile

    def lab_display(self, window):
        """
        This method loads the images from "constants" 
        and place them on structure
        """
        # convert needed sprite images
        WALL = pygame.image.load(WALL_IMG).convert_alpha()
        DEPARTURE = pygame.image.load(DEPARTURE_IMG).convert_alpha()
        NEEDLE = pygame.image.load(NEEDLE_IMG).convert_alpha()
        ALCOHOL = pygame.image.load(ALCOHOL_IMG).convert_alpha()
        GUARDIAN = pygame.image.load(GUARDIAN_IMG).convert_alpha()
        TOILET_TUBE = pygame.image.load(TOILET_TUBE_IMG).convert_alpha()
        
        # line's counter init      
        line = 0
        
        # List of each line
        for ligne in self.structure:
            # case's counter init
            case = 0
            
            # List of each sprite for each line
            for sprite in ligne:

                # Define the dimension of a box (sprite)
                y = case * SPRITE_SIDE_SIZE
                x = line * SPRITE_SIDE_SIZE
                
                
                # Choice of sprite according to the discovered letter
                if sprite == 'w':
                    window.blit(WALL, (y, x))
                elif sprite == 'D':
                    window.blit(DEPARTURE, (y, x))
                elif sprite == 'N':
                    window.blit(NEEDLE, (y, x))
                elif sprite == 'A':
                    window.blit(ALCOHOL, (y, x))
                elif sprite == "G":
                    window.blit(GUARDIAN, (y, x))
                elif sprite == 'T':
                    window.blit(TOILET_TUBE, (y, x))
                
                # Incrementation of the counters 
                # to advance in the course of the structure 
                # with a step of 1 (case & line)
                case += 1
            line += 1
