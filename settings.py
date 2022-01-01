#################################
# CREATING A SETTINGS CLASS
##################################
class Settings():
    # settings stored for Alien Invasion:

    def __init__(self):
        # SCREEN SETTINGS
        self.screen_width = 640
        self.screen_height = 480
        self.bg_color = (230,230,230)

        # BULLET SETTINGS
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bulelt_color = (60,60,60)

        # SHIP SETTINGS
        self.ship_speed_factor = 1.5