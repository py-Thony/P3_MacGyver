# -*- coding: utf-8 -*-


import pygame
# from pygame.locals import *

# Importing only what is necessary limits the loading in memory
from Data.constants import numb_sprites_side, sprite_size, mac_img, one_item_img, two_items_img, three_items_img, alcohol_img, needle_img, toilet_tube_img, syringe_img, backpack_img, four_items_img

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
        self.picture = pygame.image.load(mac_img).convert_alpha()
        self.x = self.case_x * sprite_size
        self.y = self.case_y * sprite_size
        
    def move(self, direction):
        """
        Method that defines the action of moving the character.
                - We take the width or height of the labyrinth (represented via
                  the number of cases, 15 cases == 15 sprites == width or height)
                - We recover the value of the 'next cases' and we verify that it does not
                  it's not a wall.
                - If movement is authorized, it is validated
        """

        if direction == "right":           
            if self.case_y < (numb_sprites_side - 1):
                if self.structure[self.case_y +1][self.case_x] != "w":
                    self.case_y += 1
                    self.y = self.case_y * sprite_size            
  
        if direction == "left":
            if self.case_y > 0:
                if self.structure[self.case_y -1][self.case_x] != "w":
                    self.case_y -= 1
                    self.y = self.case_y * sprite_size
                  
        if direction == "up": 
            if self.case_x > 0:
                if self.structure[self.case_y][self.case_x -1] != "w":
                    self.case_x -= 1
                    self.x = self.case_x * sprite_size
                   

        if direction == "down":
            if self.case_x < (numb_sprites_side - 1):
                if self.structure[self.case_y][self.case_x +1] != "w":             
                    self.case_x += 1
                    self.x = self.case_x * sprite_size         

    def catch_sound(self):
        if len(self.backpack) == 3:
            self.sound_catch_item = pygame.mixer.Sound("sound/ALL_ITEMS.wav")
        else:
            self.sound_catch_item = pygame.mixer.Sound("sound/CATCH_ITEM.wav")
        self.sound_catch_item.set_volume(.2)
        self.sound_catch_item.play()

    def catch_item(self, window):
        """
        Interaction between the 'character' sprite and the 'item' sprite:
                - Image conversion to optimize pygame processing
                - If the 2 sprites overlap, item disappears from the labyrinth,
                  and appears in the backpack
        """
        needle = pygame.image.load(needle_img).convert_alpha()
        alcohol = pygame.image.load(alcohol_img).convert_alpha()
        toilet_tube = pygame.image.load(toilet_tube_img).convert_alpha()
        backpack = pygame.image.load(backpack_img).convert()
        syringe = pygame.image.load(syringe_img).convert()
        three_items = pygame.image.load(three_items_img).convert_alpha()
        two_items = pygame.image.load(two_items_img).convert_alpha()
        one_item = pygame.image.load(one_item_img).convert_alpha()
        window.blit(backpack, (0, 600))

       
        """
        Updating the backpack by successively overwriting the tuple according to the (str) recovered.
        I take this opportunity to emit a sound to symbolize the recovery action.
        """
    
        if self.structure[self.case_y][self.case_x] == "N":
            self.backpack += ("needle",)
            self.catch_sound()

        elif self.structure[self.case_y][self.case_x] == "A":            
            self.backpack += ("alcohol",)
            self.catch_sound()

        elif self.structure[self.case_y][self.case_x] == "T":
            self.backpack += ("toilet_tube",)
            self.catch_sound()


        for elem in self.backpack:

            if elem == "needle":
                window.blit(needle, (380, 600))
            if elem == "toilet_tube":
                window.blit(toilet_tube, (480, 600))
            if elem == "alcohol":
                window.blit(alcohol, (520, 600))


            if len(self.backpack) == 3:
                # Blit an empty backpack 
                # (to delete the images already present)
                window.blit(backpack, (0, 600))
                # Blit new pics in backpack
                window.blit(three_items, (210, 600))
                window.blit(syringe, (380, 600))

            if len(self.backpack) == 2:
                window.blit(two_items, (210, 600))

            if len(self.backpack) == 1:
                window.blit(one_item, (210, 600))
