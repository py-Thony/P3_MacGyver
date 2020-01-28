#!/usr/bin/python3
# -*- coding: Utf-8 -*-

import pygame

# Importing only what is necessary limits the loading in memory
from Data.constants import SPRITE_NUMB_SIDE, SPRITE_SIDE_SIZE, MAC_IMG, ONE_ITEM_IMG, \
    TWO_ITEMS_IMG, THREE_ITEMS_IMG, ALCOHOL_IMG, NEEDLE_IMG, TOILET_TUBE_IMG, SYRINGE_IMG, \
    BACKPACK_IMG, ALL_ITEMS_IMG, WAV_ALL_ITEMS, WAV_CATCH_ITEM

class Character:
    """
    Class to create the characters whith name,
    initial position, valid moves and catch items.
    """
     
    def __init__(self, name, structure, position):
        """ It does not seem useful to me to comment on these lines because it seems obvious to me but:
                    - self defines the variable instead of the argument of the definition.
                    - name, structure, position, case, backpack, picture, pygame
                      express what they correspond to.
                    - backpack = () is an 'empty' tuple, a tuple cannot be modified,
                      it will therefore be replaced by a new tuple (with the same name to overwrite it)
                      as it evolves in the program.
        """
        self.name = name
        self.position = position
        self.structure = structure
        self.case_y = position[0]
        self.case_x = position[1]
        backpack = ()
        self.backpack = backpack
        self.structure[self.case_y][self.case_x] = "M"
        self.picture = pygame.image.load(MAC_IMG).convert_alpha()
        self.x = self.case_x * SPRITE_SIDE_SIZE
        self.y = self.case_y * SPRITE_SIDE_SIZE
        
    def move(self, direction):
        """
        Method that defines the action of moving the character.
                - We take the width or height of the labyrinth (represented via
                  the number of cases, 15 cases == 15 sprites == width or height)
                - We recover the value of the 'next cases' and we verify that it does not
                  it's not a wall.
                - If movement is authorized, it is validated
        """

        # Just explain for the first (right)

        # If direction == condition verified
        if direction == "right":  
            # If needed position is in the limits of number of sprite
            """
            -1 because we count from zero, 
            so if we are on box 0 and we count 15, 
            we end up on box 16
            """        
            if self.case_y < (SPRITE_NUMB_SIDE - 1):
                # If the next box is NOT a wall
                if self.structure[self.case_y +1][self.case_x] != "w":
                    # Accept the move
                    self.case_y += 1
                    # Move with width of a sprite
                    self.y = self.case_y * SPRITE_SIDE_SIZE            
  
        if direction == "left":
            if self.case_y > 0:
                if self.structure[self.case_y -1][self.case_x] != "w":
                    self.case_y -= 1
                    self.y = self.case_y * SPRITE_SIDE_SIZE
                  
        if direction == "up": 
            if self.case_x > 0:
                if self.structure[self.case_y][self.case_x -1] != "w":
                    self.case_x -= 1
                    self.x = self.case_x * SPRITE_SIDE_SIZE
                   

        if direction == "down":
            if self.case_x < (SPRITE_NUMB_SIDE - 1):
                if self.structure[self.case_y][self.case_x +1] != "w":             
                    self.case_x += 1
                    self.x = self.case_x * SPRITE_SIDE_SIZE         


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
