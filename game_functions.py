import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        #move the ship to the right
        ship.moving_right = True
        
    elif event.key == pygame.K_LEFT:
        #move the ship to the left
        ship.moving_left = True
    
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    
    elif event.key == pygame.K_q:
         sys.exit()

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

def get_number_aliens_x(ai_settings, alien_width):
    # determine the number of aliens that fit in a row
    available_space_x = ai_settings.screen_width -2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    # determine the number of rows of laiens that fit on the screen
    available_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
    number_of_rows = int(available_space_y/(2*alien_height))
    return number_of_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width+2 *alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 *alien.rect.height*row_number
    aliens.add(alien)




def create_fleet(ai_settings, screen, ship, aliens):
    # create a full fleet of aliens
    # create an alien and find the number of aliens in a row
    # spacing between each alien is equal to one alien width

    alien = Alien(ai_settings, screen)
    
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # create the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)



def update_screen(ai_settings, screen, ship, aliens, bullets):
    # update images on the screen and flip to the new screen.
    screen.fill(ai_settings.bg_color) #fill in the background with background color

    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    #alien.blitme()

    # recently draw screen is visible
    pygame.display.flip()