###########################
# IMPORT LIBRARIES/ MODULES
###########################
import sys
import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien


###########################
# FUNCTIONS: RUN_GAME
###########################
def run_game():
    pygame.init() #init game and create a screen object
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_height,ai_settings.screen_width)) #1200px wide 800px height
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    ship = Ship(ai_settings, screen)
    # make an alient
    alien = Alien(ai_settings, screen)

    # create a group to store bullets, aliens
    bullets = Group()
    aliens = Group()

    # create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()

        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen, ship, aliens, bullets)
        


run_game()
