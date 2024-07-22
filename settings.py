class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.button_color = (0, 200, 0)
        self.text_color = (255, 255, 255)
        
# # TODO: test laser with a really wide laser
        self.laser_width = 10
        self.laser_height = 30
        self.laser_color = 255, 0, 0
        self.lasers_every = 10           # change to 1 to see faster lasers

        self.aliens_shoot_every = 80    # about every 2 seconds at 60 fps

# # TODO: set a ship_limit of 3
        self.ship_limit = 3         # total ships allowed in game before game over

        self.fleet_drop_speed = 3
        self.fleet_direction = 1     # change to a Vector(1, 0) move to the right, and ...
        self.initialize_speed_settings()

    def initialize_speed_settings(self):
        self.alien_speed = 1
        self.ship_speed = 3
        self.fleet_drop_speed = 3
        self.alien_laser_speed = 3
        self.ship_laser_speed = 5
        self.speedup_scale = 1.05

    def increase_speed(self):
        scale = self.speedup_scale
        self.ship_speed *= scale
        self.speedup_scale *= scale
        self.alien_laser_speed *= scale
        self.ship_laser_speed *= scale
