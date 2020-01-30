#!/usr/bin/python3
# -*- coding: Utf-8 -*-

import pygame

# Importing only what is necessary limits the loading in memory
from Data.constants import SPRITE_NUMB_SIDE, SPRITE_SIDE_SIZE, MAC_IMG, ONE_ITEM_IMG, \
    TWO_ITEMS_IMG, THREE_ITEMS_IMG, ALCOHOL_IMG, NEEDLE_IMG, TOILET_TUBE_IMG, SYRINGE_IMG, \
    BACKPACK_IMG, ALL_ITEMS_IMG, WAV_ALL_ITEMS, WAV_CATCH_ITEM



##################################
##################################
##################################


class Sprite:
    """
    Class to create the sprites
    """
    #         backpack = ()
    #    self.backpack = backpack
        

    def __init__(self, sprite_name, sprite_letter, sprite_position, sprite_image, maze_structure):

        self.sprite_name = sprite_name[0]

        self.maze_structure = maze_structure

        self.sprite_position = sprite_position
        self.sprite_position_y = sprite_position[0]
        self.sprite_position_x = sprite_position[1]
        
        self.maze_structure[self.sprite_position_y][self.sprite_position_x] = sprite_letter
        
        self.sprite_image = sprite_image 
        
        self.sprite_position_x = self.sprite_position_x * SPRITE_SIDE_SIZE
        self.sprite_position_y = self.sprite_position_y * SPRITE_SIDE_SIZE

    

    def move_sprite(self, sprite_direction):

        """
        Method that defines the action of moving the sprite

        """
        # BEFORE MODIFYING, or for understanding:
        #           See 'Particular_things_move.txt' in the 'Notes' folder 
        #           for all informations about this list comprehension.
        self.sprite_direction = sprite_direction
        self.sprite_direction == [ 

                [
                
                    self.next_position for self.next_position in 

                        ( 
        
                        self.maze_structure[self.sprite_position_y][self.sprite_position_x] > 0 
        
                        and

                        self.maze_structure[self.sprite_position_y][self.sprite_position_x] < SPRITE_NUMBER_SIZE

                        )
                ]

                for self.maze_struture in labyrinth
            
            ]
            

##################################
##################################
##################################      
       


    def catch_sound(self):
        """
        Materialize the taking of object by a sound
        A sound for a recovered object, 
        and another sound when all the items are recovered
        """

        # Condition for all recovered objects
        if len(self.backpack) == 3:
            # load simple sound
            self.sound_catch_item = pygame.mixer.Sound(WAV_ALL_ITEMS)
        # While all objects are not recovered
        else:
            # Load simple sound
            self.sound_catch_item = pygame.mixer.Sound(WAV_CATCH_ITEM)
        
        # Control volume
        self.sound_catch_item.set_volume(.1)
        # Playing sound
        self.sound_catch_item.play()

    def catch_item(self, window):
        """
        Interaction between the 'character' sprite and the 'item' sprite:
                - Image conversion to optimize pygame processing
                - If the 2 sprites overlap, item disappears from the labyrinth,
                  and appears in the backpack
        """
        NEEDLE = pygame.image.load(NEEDLE_IMG).convert_alpha()
        ALCOHOL = pygame.image.load(ALCOHOL_IMG).convert_alpha()
        TOILET_TUBE = pygame.image.load(TOILET_TUBE_IMG).convert_alpha()
        BACKPACK = pygame.image.load(BACKPACK_IMG).convert()
        SYRINGE = pygame.image.load(SYRINGE_IMG).convert()
        THREE_ITEMS = pygame.image.load(THREE_ITEMS_IMG).convert_alpha()
        TWO_ITEMS = pygame.image.load(TWO_ITEMS_IMG).convert_alpha()
        ONE_ITEM = pygame.image.load(ONE_ITEM_IMG).convert_alpha()
        window.blit(BACKPACK, (0, 600))

       
        """
        Updating the backpack by successively overwriting the tuple according to the recovered.
        I take this opportunity to emit a sound to symbolize the recovery action.
        """

        # Just explain for the first

        # If the letter is found in the list of lists 
        if self.structure[self.case_y][self.case_x] == "N":
            # Collage of the corresponding image in the backpack
            self.backpack += ("needle",) # Finish by ',' (tuple)
            
            #Call good sound to play in catch_sound()
            self.catch_sound()

        elif self.structure[self.case_y][self.case_x] == "A":            
            self.backpack += ("alcohol",)
            self.catch_sound()

        elif self.structure[self.case_y][self.case_x] == "T":
            self.backpack += ("toilet_tube",)
            self.catch_sound()


        # Loop for list the elements in backpack
        for elem in self.backpack:
            
            # For each element, collage at the defined position 
            if elem == "needle":
                window.blit(NEEDLE, (380, 600))
            if elem == "toilet_tube":
                window.blit(TOILET_TUBE, (480, 600))
            if elem == "alcohol":
                window.blit(ALCOHOL, (520, 600))

            # Condition for all recovered objects
            if len(self.backpack) == 3:
                # Blit an empty backpack 
                # (to delete the images already present)
                window.blit(BACKPACK, (0, 600))
                # Blit new images in backpack
                window.blit(THREE_ITEMS, (210, 600))
                window.blit(SYRINGE, (380, 600))

            # Condition for two recovered objects
            if len(self.backpack) == 2:
                window.blit(TWO_ITEMS, (210, 600))

            # Condition for only one recovered object
            if len(self.backpack) == 1:
                window.blit(ONE_ITEM, (210, 600))
