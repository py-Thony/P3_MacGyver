#!/usr/bin/python3
# -*- coding: Utf-8 -*-

"""
MAIN GAME PAGE
Script Python
"""

# Import of the GameLoops class from game_loops into Data
from Data.game_loops import GameLoops

# Simplification of the class name 
# for the subsequent call to the home_loops method
LOOP = GameLoops()

"""
    Starting the program minimized by simply launching the game loop
"""

# Simplified call (home_loops () method of the GameLoops () class)
LOOP.home_loops()
LOOP.game_loops()
