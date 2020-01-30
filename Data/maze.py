#!/usr/bin/python3
# -*- coding: Utf-8 -*-

"""

#####
PEP 8
#####

|-------------------------Max width of comments------------------------|
|-------------------------Max width of the code-------------------------------|


""""""

#############
AGIL PRACTICE
#############      The mess should be seen as a bug in its own right


Changes to the code must be made in accordance with the 'clean code' rule

Each modification must give an improvement as the first visible result.
The developer making a change should ask the following question:

    Will the change I'm looking for make to the code:

                - Better readability or overall understanding of operation ?
                
                - A gain in productivity by allowing easier later modifications ?

"""



# Importing only what is necessary will minimize the loading in memory.
#
# The reward for the developer is that in a single line 
# he can know the complete list of interactions without even reading the code.
import pygame

from pygame.locals import *

from random import randint

from Data.constants import WALL_IMG, DEPARTURE_IMG, NEEDLE_IMG, ALCOHOL_IMG, \
                           GUARDIAN_IMG, TOILET_TUBE_IMG, SPRITE_SIDE_SIZE, \
                           DRAW_FILE

class Maze:

    """
    This class is to initialize the game board
    from the file "structure" wich contains the structure of the 
    labyrinth,and choose ramdomly a free space on the structure
    """



    def __init__(self):

        """
        Using conditional list comprehension in a for loop
        https://blog.tecladocode.com/python-list-comprehensions-conditionals/
        """

        with open(DRAW_FILE, 'r') as labyrinth:

            self.maze_structure = [

                [maze_letter for maze_letter in maze_line if maze_letter != "\n"] 
                
                for maze_line in labyrinth
            ]


##################################
##################################
##################################

    def sprite_creation(self, sprite_letter, sprite_image):

        """
        Tous les sprites nécessitent la même méthode:

        Choisir où placer le sprite
        en retournant sa position de départ et l'image à afficher

        """
           
        for self.sprite_position_y, maze_line in enumerate(self.maze_structure):

            for self.sprite_position_x, sprite_letter in enumerate(maze_line):

                if self.maze_structure[self.sprite_position_y][self.sprite_position_x] == sprite_letter:
                    self.sprite_position = self.sprite_position_y, self.sprite_position_x
                    self.sprite_image = pygame.image.load(sprite_image).convert_alpha()

                    return self.sprite_position, self.sprite_image

##################################
##################################
##################################


    def sprite_choice_image(self, sprite_letter, sprite_image):
        # REDONDANCE de sprite_image
        # Le sprite appelle déjà son affichage dans move
        """
        Un sprite se résume à être une image affichée

        Pour différencier un sprite d'un autre, nous n'avons besoin
        que de définir son "identité" par la première lettre de son nom.

        Pour choisir la bonne image à afficher nous n'avons besoin que de faire
        correspondre une méthode d'appel liée à ce nom
        """

        self.sprite_name[0] = sprite_letter

        self.maze_structure = maze_structure

        self.sprite_position = sprite_position
        self.sprite_position_y = sprite_position[0]
        self.sprite_position_x = sprite_position[1]

        self.maze_structure[self.sprite_position_y][self.sprite_position_x] = sprite_name[0]

        return sprite_position




    def place_sprite_in_maze(self):

        """
        Random positioning, provided that the location is an empty box.
        If the box is not empty, the search is restarted.
        """

        random_line_of_maze = randint(0, len(self.maze_structure) -1)
        random_tile_of_maze = randint(0, len(self.maze_structure[random_line_of_maze]) -1)
        place_object_in_maze = self.maze_structure[random_line_of_maze][random_tile_of_maze]

        while place_object_in_maze != " ":
            
            random_tile_of_maze = randint(0, len(self.maze_structure[random_line_of_maze]) -1)
            place_object_in_maze = self.maze_structure[random_line_of_maze][random_tile_of_maze]
        
        return random_line_of_maze, random_tile_of_maze




    def sprite_display(self, window):

        """
        This method loads the images from "constants" 
        and place them on structure
        """

        WALL = pygame.image.load(WALL_IMG).convert_alpha()
        DEPARTURE = pygame.image.load(DEPARTURE_IMG).convert_alpha()
        NEEDLE = pygame.image.load(NEEDLE_IMG).convert_alpha()
        ALCOHOL = pygame.image.load(ALCOHOL_IMG).convert_alpha()
        GUARDIAN = pygame.image.load(GUARDIAN_IMG).convert_alpha()
        TOILET_TUBE = pygame.image.load(TOILET_TUBE_IMG).convert_alpha()
        
   
        line = 0

        for ligne_of_maze in self.maze_structure:

            case_of_maze = 0

            for sprite_letter in ligne:

                y = case_of_maze * SPRITE_SIDE_SIZE
                x = line_of_maze * SPRITE_SIDE_SIZE

                if sprite_letter == sprite_letter:
                    window.blit(sprite_image, (y, x))
                
                # Incrementation of the counters 
                # to advance in the course of the structure 
                # with a step of 1 (case & line)
                case += 1
            line += 1
