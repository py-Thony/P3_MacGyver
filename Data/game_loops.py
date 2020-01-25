import os
import pygame
from pygame.locals import *
import Data.constants
from Data.labyrinth import Labyrinth
from Data.character import Character
#from Data.guardian import Guardian
#from Data.item import Item

pygame.init() # Initialisation du module Pygame

class GameLoops: # Définition de la classe de jeu principal
    """
    Creation of all loops game
    Les commentaires sont pour la plupart évidents, ils ne sont justifiés que pour la démonstration
    d'une parfaite compréhension du code étant donné qu'il s'agit d'un TP.
    """

    def __init__(self):

        """
        Creation of the main window and game sounds.
        """
        os.environ['SDL_VIDEO_CENTERED'] = '1' # Centrage de la fenêtre ( Doit être appelé avant)
        self.window = pygame.display.set_mode((600, 640))                  # Format de la fenêtre
        icon = pygame.image.load(Data.constants.ICON_IMG)                   # Icône de la fenêtre
        pygame.display.set_icon(icon)                                      # Affichage de l'icône
        pygame.display.set_caption(Data.constants.Title)       # Affichage du titre de la fenêtre
        pygame.key.set_repeat(400, 30)
        self.sound = pygame.mixer.Sound("sound/Mac.wav")                      # Musique d'accueil
        # Réglage du volume à la baisse (Musique d'origine trop forte)
        self.sound.set_volume(.1)
        self.sound_game = pygame.mixer.Sound("sound/game.wav")            # Musique du labyrinthe
        self.sound_loose = pygame.mixer.Sound("sound/loose.wav")              # Musique Game Over
        self.sound_win = pygame.mixer.Sound("sound/win.wav")                   # Musique victoire
        self.game_loop = True                  # Affectation de valeur "vraie" à la boucle de jeu
        self.home_loop = True            # Affectation de valeur "vraie" à la boucle de l'accueil

    def home_loops(self):                                  # Définition de la boucle de l'accueil
        """
        Home loop for the welcome window with sound.
        """
        # Chargement et conversion du fond d'écran (Accueil et Sac à dos)
        HOME_PIC = pygame.image.load(Data.constants.HOME_PIC).convert() 
        backpack_start = pygame.image.load(Data.constants.backpack_start).convert_alpha()

        # self.home_loop = True                                     # Boucle de l'accueil sur "vrai"
        self.game_loop = False       # Boucle de jeu sur "Faux" (sera vrai quand Home sera "faux")
        
        while self.home_loop:                                         # Tant que home_loop == True
            
            self.window.blit(HOME_PIC, (0, 0))                        # Collage de l'image de fond
            self.window.blit(backpack_start, (0, 600))
            self.sound.set_volume(.05)
            self.sound.play()                            # Activation de la musique de fond

            for event in pygame.event.get():             # Pour tout évennement détecté par Pygame
                
                if event.type == QUIT:       # Si l'évennement est un clic sur la croix de fenêtre
                    self.home_loop = False                         # Fin de la boucle de l'accueil
                    self.game_loop = False                             # Arrêt de la boucle de jeu
                
                elif event.type == KEYDOWN:                 # Dans le cas d'une pression de touche
                    
                    if event.key == K_ESCAPE:                           # Si la touche est "Echap"
                        self.game_loop = False                         # Arrêt de la boucle de jeu
                        self.home_loop = False                   # Arrêt de la boucle de l'accueil 
                    
                    elif event.key == K_RETURN:                           # Si la touche est ENTREE
                        self.game_loop = True                            # Boucle de jeu sur "Vrai"
                        self.home_loop = False                      # Fin de la boucle de l'accueil
                        pygame.mixer.stop() # Arrêt de la musique pour pouvoir démarrer la suivante

            pygame.display.flip() # Rafraichissement de la fenêtre pour afficher les collages à jour

    def game_loops(self):                                           # Définition de la boucle de jeu
        """
        Main game loop
        Creation of game structure, characters and items.
        """
        BACK_GROUND = pygame.image.load(Data.constants.BACK_IMG).convert_alpha()       # Background of Laby.
        backpack_win = pygame.image.load(Data.constants.backpack_win).convert_alpha()   # Backpack (Victory)
        backpack_loose = pygame.image.load(Data.constants.backpack_loose).convert_alpha() # Backpack (loose)
        win_img = pygame.image.load(Data.constants.win_img).convert_alpha()           # Background (Victory)
        loose_img = pygame.image.load(Data.constants.youloose_img).convert_alpha()  # Background (game over)
        lab = Labyrinth()                                                           # Var == Class Labyrinth
        lab.lab_display(self.window)                                                # Affichage du labyrinth
        Mac = Character("Mac", lab.structure, lab.character_position("D"))      #Place MacGyver
        Guardian = Character("Guardian", lab.structure, lab.character_position("A"))    # Place Guardian
        needle = lab.item("Needle", lab.structure, lab.place_object_in_maze())            # Item #1 position aléatoire
        alcohol = lab.item("Alcohol", lab.structure, lab.place_object_in_maze())          # Item #2 position aléatoire
        toilet_tube = lab.item("Toilet_tube", lab.structure, lab.place_object_in_maze())  # Item #3 position aléatoire

        
        # La valeur de self.home.loop == False est connue grâce à home_loops()
        #La valeur de self.game_loop = True est connue grâce à home_loops()      
        while self.game_loop:                        # Tant que la condition de la boucle de jeu est "vraie"
            #pygame.mixer.unpause()                                                # Son en pause avant appel
            # Réglage sonore (lecture en boucle avec fin en fondu)
            self.sound_game.set_volume(.07)
            self.sound_game.play(loops=1, maxtime=0, fade_ms=50)

            # Blocage du taux de rafraichissement pour éviter surload Processeur
            pygame.time.Clock().tick(60) 
            lab.lab_display(self.window) # Affichage du labyrinth dans la fenêtre
            lab.structure[Mac.case_y][Mac.case_x] = " " # 'Case vide' pour autoriser déplacement personnage
            for event in pygame.event.get(): # Possibilité de quitter....
                if event.type == QUIT:
                    self.game_loop = False
                    self.home_loop = True
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.game_loop = False
                        self.home_loop = True
                    # mouvements avec les flèches clavier
                    elif event.key == K_DOWN:
                        Mac.move('right')
                    elif event.key == K_UP:
                        Mac.move('left')
                    elif event.key == K_LEFT:
                        Mac.move('up')
                    elif event.key == K_RIGHT:
                        Mac.move('down')
            pygame.display.flip() # Rafraichissement de la fenêtre

            if lab.structure[Mac.case_y][Mac.case_x] == "G": # Quand Mac rencontre le gardien
                self.game_loop = False # Fin de la boucle de jeu
                pygame.mixer.stop() # Arrêt de la musique pour pouvoir démarrer la suivante
                if len(Mac.back_pack) == 3: # Test de la récupération des 4 Items
                    win = True # Victoire est "vraie" si les Items sont collectés
                    self.sound_win.play() # Jouer le son de victoire
                    self.sound_win.set_volume(.09) # Réglage du volume sur "audible mais pas trop"
                    while win: # Dans le cas de victoire                            
                        self.window.blit(win_img, (0, 0)) # Collage de l'image de victoire
                        self.window.blit(backpack_win, (0, 600))
                        pygame.display.flip() # Rafraichissement de l'image
                        for event in pygame.event.get(): # Possibilité de quitter....
                            if event.type == QUIT:
                                win = False
                            elif event.type == KEYDOWN:
                                # Echap por quitter
                                if event.key == K_ESCAPE:
                                    win = False
                elif len(Mac.back_pack) != 3: # Dans le cas où les Items ne sont pas tous récupérés
                    self.sound.stop() # Arrêt de la musique
                    loose = True # Activation scénario défaite
                    self.sound_loose.play() # Jouer le son de la défaite ( Sorti de la boucle)
                    self.sound_loose.set_volume(.09) # Réglage du volume sur "audible mais pas trop"
                    while loose: # Si défaite...
                        self.window.blit(loose_img, (0, 0)) # Collage de l'image de défaite
                        self.window.blit(backpack_loose, (0, 600))
                        pygame.display.flip() # Rafraichissement de la fenêtre
                        for event in pygame.event.get(): # Possibilité de quitter....
                            if event.type == QUIT:
                                loose = False
                            elif event.type == KEYDOWN or event.type == KEYUP:
                                # Echap pour quitter
                                if event.key == K_ESCAPE:
                                    loose = False


            self.window.blit(BACK_GROUND, (0, 0)) # Collage du fond du labyrinth
            lab.lab_display(self.window) # Affichage du labyrinth dans la fenêtre
            self.window.blit(Mac.picture, (Mac.x, Mac.y)) # Collage du personnage dans le labyrinth
            Mac.catch_item(self.window) # Appel de la définition de récupération d'objet
            lab.structure[Mac.case_y][Mac.case_x] = "M" # Association du personnage à "M" (Lecture de la Map)
            lab.structure[Guardian.case_y][Guardian.case_x] = "G" # Association du personnage à "G" (Lecture de la Map)
            pygame.display.flip() # Rafraichissement de la fenêtre
