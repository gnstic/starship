import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # CLASS TO MANAGE BULLET FIRED FROM THE SHIP

    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        # create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullet position as a decimcal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # MOVE THE BULLET UP THE SCREEN
        self.y -= self.speed_factor
        # UPDATE THE RECT POSITION
        self.rect.y = self.y

    def draw_bullet(self):
        # DRAW THE BULLET TO THE SCREEN
        pygame.draw.rect(self.screen, self.color, self.rect)