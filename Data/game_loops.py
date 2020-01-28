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

import os                                 # For interaction with system
                                      # For SDL gestion (video centerd)

import pygame                                 # For gestion of graphics

from pygame.locals import *                      # Submodules of pygame

"""
Importing only what is necessary reduces the loading in memory.
The second advantage resides in the fact of knowing the state of each 
variable (via pylint in VScode) when the code is updated.

And obliging to an additional rigor concerning the control of code.
"""

# IMport the necessary variables (uppercases for variables)
from Data.constants import ICON_IMG, TITLE, Y_SIZE_WINDOW, X_SIZE_WINDOW, \
                           DELAY, INTERVAL, HOME_IMG, BACK_IMG, LOOSE_IMG, \
                           BACKPACK_HOME_IMG, BACKPACK_WIN_IMG, WIN_IMG, \
                           BACKPACK_LOOSE_IMG, WAV_LOOSE, FPS, GAME_WAV, \
                           MAC_WAV

# Import the structure and settings of the labyrinth
from Data.labyrinth import Labyrinth

# Import the caracterics of positions and moves of characters
from Data.character import Character
# Initialization of Pygame's modules
pygame.init()

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

class GameLoops:                         # Definition of principal loop
    """
    Creation of all loops game
    The comments are often obvious, they are only justified to 
    demonstrate a perfect understanding of the code because it's a T.P.
    """

    def __init__(self):

        """
        Creation and settings of the main window and key.events.
        """
        
        # Window centering (Must be called before)
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        # Window format
        self.window = pygame.display.set_mode((Y_SIZE_WINDOW, X_SIZE_WINDOW))
        ICON = pygame.image.load(ICON_IMG)                # Window icon
        pygame.display.set_icon(ICON)                    # Icon display
        pygame.display.set_caption(TITLE)        # Window title display
        
        # Keys that are held down 
        # will generate multiple pygame.KEYDOWN events
        pygame.key.set_repeat(DELAY, INTERVAL) 
    
        self.game_loop = True            # define var before assignment
        self.home_loop = True            # define var before assignment

    def home_loops(self):                 # Definition of the home loop
        
        """
        Home loop for the welcome window with sound.
        """
        
        # Loading and converting the wallpaper (Home and Backpack)
        HOME_BACKGROUNG = pygame.image.load(HOME_IMG).convert() 
        HOME_BACKPACK = pygame.image.load(BACKPACK_HOME_IMG).convert_alpha()

        # self.home_loop = True 
        # (The value is returned from the constructor of Class)

        # Game loop on 'False' (will be true when Home is 'false')
        self.game_loop = False

        # Loading of the music before use
        self.sound = pygame.mixer.music.load(MAC_WAV)
        # Volume control down (Original music too loud)
        pygame.mixer.music.set_volume(.2)
        # Playing music
        self.sound = pygame.mixer.music.play()

        # Instructions to follow as long as the loop is true
        while self.home_loop:

            # Collage of the images
            # (game zone)            
            self.window.blit(HOME_BACKGROUNG, (0, 0))
            # (bottom zone)
            self.window.blit(HOME_BACKPACK, (0, 600))

            # For any event detected by Pygame
            for event in pygame.event.get():
                
                # In the case of a click on the window cross
                if event.type == QUIT:
                    self.home_loop = False             # Stop home loop
                    self.game_loop = False             # Stop game loop
                
                # In the case of a key press
                elif event.type == KEYDOWN:
                    
                    # If key press == escape
                    if event.key == K_ESCAPE:
                        self.game_loop = False         # Stop game loop
                        self.home_loop = False         # Stop home loop
                    
                    # If key press == return
                    elif event.key == K_RETURN:
                        self.game_loop = True           # RUN game loop
                        self.home_loop = False         # Stop home loop
                        
                        """
                        Only one music can be played at a time, 
                        otherwise you have to use the queue.

                        So it's easier to just stop the music playing 
                        before loading the news.
                        """
                        pygame.mixer.music.stop()

            # Refresh the window to display the updated collages
            pygame.display.flip()

    def game_loops(self):                 # Definition of the game loop
        
        """
        Main game loop
        Creation of game structure, characters and items.
        """
        
        # Background of Laby.
        BACKGROUND = pygame.image.load(BACK_IMG).convert_alpha()
        # Backpack (Victory)
        BACKPACK_WIN = pygame.image.load(BACKPACK_WIN_IMG).convert_alpha()
        # Backpack (loose)
        BACKPACK_LOOSE = pygame.image.load(BACKPACK_LOOSE_IMG).convert_alpha()
        # Background (Victory)
        WIN = pygame.image.load(WIN_IMG).convert_alpha()
        # Background (game over)
        LOOSE = pygame.image.load(LOOSE_IMG).convert_alpha()
        
        # Simplifies entering the class name
        lab = Labyrinth()
        # Labyrinth display
        lab.lab_display(self.window)

        # Assignment of the characteristics inherited from the 
        # character&Labyrinth classes to the different variables.
        #
        # Demonstration of understanding the cutting of code line too long
        MAC = Character(
            "Mac", 
            lab.structure, 
            lab.character_position("D")
        )

        GUARDIAN = Character(
            "Guardian", 
            lab.structure, 
            lab.character_position("A")
        )

        NEEDLE = lab.item(
            "Needle", 
            lab.structure, 
            lab.place_objects_in_maze()
        )

        ALCOHOL = lab.item(
            "Alcohol", 
            lab.structure, 
            lab.place_objects_in_maze()
        )

        TOILET_TUBE = lab.item(
            "Toilet_tube", 
            lab.structure, 
            lab.place_objects_in_maze()
        )
        
        # Volume control down (Original music too loud)
        pygame.mixer.music.set_volume(.3)
        # Loading music
        self.sound_game = pygame.mixer.music.load(GAME_WAV)
        # Playing music
        self.sound_game = pygame.mixer.music.play() 


        # self.home.loop == False is known thanks to home_loops ()
        # self.game_loop = True is known thanks to home_loops()      
        
        # Instructions to follow as long as the loop is true
        while self.game_loop:

            # Blocking the refresh rate to avoid processor overload
            # 30 FPS is sufficient for refreshment
            pygame.time.Clock().tick(FPS)

            # Labyrinth display
            lab.lab_display(self.window)
            # 'Empty box' to allow character movement
            lab.structure[MAC.case_y][MAC.case_x] = " "

            # Already explained in home_loops()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game_loop = False
                    self.home_loop = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.game_loop = False
                        self.home_loop = False
                    
                    # If a keyboard arrow is pressed,
                    # call of the move function 
                    # corresponding to the corresponding arrow
                    elif event.key == K_DOWN:
                        MAC.move('right')
                    elif event.key == K_UP:
                        MAC.move('left')
                    elif event.key == K_LEFT:
                        MAC.move('up')
                    elif event.key == K_RIGHT:
                        MAC.move('down')
            
            # Refresh the window to update the collages
            pygame.display.flip()

            # When MacGyver meets the Guardian
            if lab.structure[MAC.case_y][MAC.case_x] == "G":

                # The game is over, end of the game loop
                self.game_loop = False 

                # Stop Game music
                pygame.mixer.stop()

                # Test of the recovery of the 3 Items
                # victory is 'true' if Items are all collected
                if len(MAC.backpack) == 3:
                    win = True

                    # Loading music of victory
                    self.sound_win = pygame.mixer.music.load("sound/win.wav")
                    # Volume control 
                    pygame.mixer.music.set_volume(.1)
                    # Playing music
                    pygame.mixer.music.play()  

                    # As long as the condition is fulfilled
                    while win:

                        # Collage of the game zone
                        self.window.blit(WIN, (0, 0))
                        # Collage of the bottom zone
                        self.window.blit(BACKPACK_WIN, (0, 600))

                        # Display refresh
                        pygame.display.flip()


                        # Home and game loops are already stopped, 
                        # so just stop the current loop (win loop)
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                win = False
                            elif event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    win = False

                # Test of the recovery of the 3 Items
                # loose is 'true' if Items are not all collected                                    
                elif len(MAC.backpack) != 3:
                    loose = True

                    # Loading loose music
                    self.sound_loose = pygame.mixer.music.load(WAV_LOOSE)
                    # Control volume
                    pygame.mixer.music.set_volume(.1)
                    # Playing music
                    pygame.mixer.music.play()


                    # As long as the condition is fulfilled
                    while loose:
                        # Collage of the game zone
                        self.window.blit(LOOSE, (0, 0))
                        # Collage of the bottom zone
                        self.window.blit(BACKPACK_LOOSE, (0, 600))
                        
                        # Display refresh
                        pygame.display.flip()
                        
                        # Home and game loops are already stopped, 
                        # so just stop the current loop (win loop)
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                loose = False
                            elif event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    loose = False


            # End of block (When MacGyver meets the Guardian)
            # For win or loose scenary

            # Collage of background
            self.window.blit(BACKGROUND, (0, 0))
            # Labyrinth display
            lab.lab_display(self.window)
            # Collage of character
            self.window.blit(MAC.picture, (MAC.x, MAC.y))
            # Call method for catch items
            MAC.catch_item(self.window)
            # Associate the character with his letter
            lab.structure[MAC.case_y][MAC.case_x] = "M"
            # Associate the guardian with his letter
            lab.structure[GUARDIAN.case_y][GUARDIAN.case_x] = "G"
            
            # Display refresh
            pygame.display.flip()
