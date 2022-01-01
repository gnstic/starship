import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    # A CLASS TO REPRESENT A SINGLE ALIEN IN THE FLEET

    def __init__(self, ai_settings, screen):
        # init the alie and set its starting position
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien exact position
        self.x = float(self.rect.x)

    def blitme(self):
        # draw the alien and its current location
        self.screen.blit(self.image, self.rect)