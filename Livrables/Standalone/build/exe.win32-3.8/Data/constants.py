#!/usr/bin/python3
# -*- coding: Utf-8 -*-


                            ##################
                            # GAME Constants #
                            ##################


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


########################
# PARAMS OF THE WINDOW #
########################

# Title of the window
TITLE = " Aidez MacGyver à s'échapper du labyrinthe !"

# Icon of the window
ICON_IMG = "pics/icon.png"

# Variables needed to calculate dimensions (window, sprite)
SPRITE_NUMB_SIDE = 15
SPRITE_SIDE_SIZE = 40
Y_SIZE_WINDOW = 600
X_SIZE_WINDOW = 640 

# Refresh
FPS = 30



####################
# EVENTS OF PYGAME #
####################

# pygame.key.set_repeat(delay, interval)
DELAY = 100
INTERVAL = 20



########
# HOME #
########

# background images
HOME_IMG = "pics/HOME_PIC.jpg"
BACK_IMG = "pics/BACK_IMG.png"



#############
# LABYRINTH #
#############

# Map of level
DRAW_FILE = "Data/draw_file"

# sprites images
MAC_IMG = "pics/Mac.png"
GUARDIAN_IMG = "pics/Guardian.png"
TOILET_TUBE_IMG = "pics/toilet_tube.png"
NEEDLE_IMG = "pics/needle.png"
ALCOHOL_IMG = "pics/alcohol.png"
SYRINGE_IMG = "pics/syringe.png"
DEPARTURE_IMG = "pics/departure.png"
WALL_IMG = "pics/WALL_IMG.png"

# end of game
WIN_IMG = "pics/YouWin.png"
LOOSE_IMG = "pics/YouLoose.png"



############
# BACKPACK #
############

# background
BACKPACK_HOME_IMG = "pics/backpack_start.png"
BACKPACK_IMG = "pics/backpack.png"
BACKPACK_WIN_IMG = "pics/backpack_win.png"
BACKPACK_LOOSE_IMG = "pics/backpack_loose.png"

# Collage
ONE_ITEM_IMG = "pics/one_item.png"
TWO_ITEMS_IMG = "pics/two_items.png"
THREE_ITEMS_IMG = "pics/three_items.png"
ALL_ITEMS_IMG = "pics/four_items.png"

###################
# MUSICS & SOUNDS #
###################

# Music
WAV_LOOSE = "sound/loose.wav"
GAME_WAV = "sound/game.wav"
MAC_WAV = "sound/Mac.wav"

# Sound
WAV_ALL_ITEMS = "sound/ALL_ITEMS.wav"
WAV_CATCH_ITEM = "sound/CATCH_ITEM.wav"