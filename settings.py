class Settings:
    """Class to store all settings from the Alien Invasion Game"""

    def __init__(self):
        """Initiate the game static settings"""
        """Execute game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (0,0,0)

        # Space ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (164, 66, 245)
        self.bullets_allowed = 5

        # Enemy bullets
        self.enemy_bullet_color = 	(124,252,0)


        # Enemy Settings
        self.fleet_drop_speed = 8.5
        # Fleet direction 1 = right / -1 = left


        # How fast the enemies will drop down
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Init settings that change through the game"""
        self.space_ship_speed = 1.5
        self.bullet_speed = 3.0
        self.enemy_speed = 1.0
        self.enemy_bullet_speed = 3

        # Fleet direction 1 = right / -1 = left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increasing the speed of the game"""
        self.space_ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.enemy_speed *= self.speedup_scale
        self.enemy_bullet_speed *= self.speedup_scale