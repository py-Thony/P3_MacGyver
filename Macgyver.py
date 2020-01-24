#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
MAIN GAME PAGE
Script Python
"""

from Data.game_loops import GameLoops # Importation de la classe GameLoops depuis game_loops dans Data

LOOP = GameLoops() # Simplification du nom de la classe pour l'appel ultérieur de la méthode home_loops

"""
    Démarrage du programme minimisé au simple lancement de la boucle de jeu
"""

LOOP.home_loops() # Appel simplifié ( Méthode home_loops() de la classe GameLoops() )
LOOP.game_loops()
