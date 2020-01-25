import pygame
from pygame.locals import *

from Data.constants import numb_sprites_side, sprite_size, mac_img, one_item_img, two_items_img, three_items_img, alcohol_img, needle_img, toilet_tube_img, syringe_img, backpack_img, four_items_img

class Character:
    """
    Class to create the characters whith name,
    initial position, valid moves and catch items.
    Je réutilise cette classe pour positionner mes Items afin de ne pas créer une classe spécialement
    pour leur positionnement. (Une classe n'est justifiée que par sa "multi" utilisation dans un programme)
    """
     
    def __init__(self, name, structure, position):
        self.name = name
        self.position = position
        self.structure = structure
        self.case_y = position[0]
        self.case_x = position[1]
        back_pack = ()
        self.back_pack = back_pack
        self.structure[self.case_y][self.case_x] = "M"
        self.picture = pygame.image.load(mac_img).convert_alpha()
        self.x = self.case_x * sprite_size
        self.y = self.case_y * sprite_size
        
    def move(self, direction):

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


    def catch_item(self, window):
        needle = pygame.image.load(needle_img).convert_alpha()
        alcohol = pygame.image.load(alcohol_img).convert_alpha()
        toilet_tube = pygame.image.load(toilet_tube_img).convert_alpha()
        back_pack = pygame.image.load(backpack_img).convert()
        syringe = pygame.image.load(syringe_img).convert()
        three_items = pygame.image.load(three_items_img).convert_alpha()
        two_items = pygame.image.load(two_items_img).convert_alpha()
        one_item = pygame.image.load(one_item_img).convert_alpha()
        window.blit(back_pack, (0, 600))

        
        if self.structure[self.case_y][self.case_x] == "N":
            self.back_pack += ("needle",)
        
        if self.structure[self.case_y][self.case_x] == "A":            
            self.back_pack += ("alcohol",)
 
        if self.structure[self.case_y][self.case_x] == "T":
            self.back_pack += ("toilet_tube",)

        for elem in self.back_pack:

            if elem == "needle":
                window.blit(needle, (380, 600))
            if elem == "toilet_tube":
                window.blit(toilet_tube, (480, 600))
            if elem == "alcohol":
                window.blit(alcohol, (520, 600))
            if len(self.back_pack) == 3:
                window.blit(back_pack, (0, 600))
                window.blit(three_items, (210, 600))
                window.blit(syringe, (380, 600))
            if len(self.back_pack) == 2:
                window.blit(two_items, (210, 600))
            if len(self.back_pack) == 1:
                window.blit(one_item, (210, 600))    
