###########################
# IMPORT LIBRARIES/ MODULES
###########################
import sys
import pygame
from settings import Settings
from ship import Ship

###########################
# FUNCTIONS: RUN_GAME
###########################
def run_game():
    pygame.init() #init game and create a screen object
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_height,ai_settings.screen_width)) #1200px wide 800px height
    bg_color = ai_settings.bg_color #set the background color
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    ship = Ship(screen)

    # start the main loop for the game
    while True:

        #watch for keyboard mouse events
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()

        screen.fill(bg_color) #fill in the background with background color
        ship.blitme()

        # recently draw screen is visible
        pygame.display.flip()

run_game()
