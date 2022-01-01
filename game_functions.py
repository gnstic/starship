import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        #move the ship to the right
        ship.moving_right = True
        
    elif event.key == pygame.K_LEFT:
        #move the ship to the left
        ship.moving_left = True
    
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen, ship, bullets):
    # respond to keypresses and mouse events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings,screen, ship, bullets)
        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_bullets(bullets):
    # UPDATE POSIITON OF BULLETS AND GET RID OF OLD BULLETS
    # UPDATE BULLET POSITIONS
    bullets.update()

    # getting rid of dissapeared bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    # FIRE A BULLET IF LIMIT NOT REACHED YET
    # create a new bullet and add it to the bullets group
    if len(bullets)< ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        
def update_screen(ai_settings, screen, ship, bullets):
    # update images on the screen and flip to the new screen.
    screen.fill(ai_settings.bg_color) #fill in the background with background color

    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # recently draw screen is visible
    pygame.display.flip()