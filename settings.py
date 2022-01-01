class Settings:
    """Class to store all settings from the Alien Invasion Game"""

    def __init__(self):
        """Execute game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (0,0,0)

        # Space ship settings
        self.space_ship_speed = 1.5

        # Bullet settings
        self.bullet_speed =  2
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (164, 66, 245)
        self.bullets_allowed = 5

        # Enemy Settings
        self.enemy_speed = 1.0
        self.fleet_drop_speed = 10
        # Fleet direction 1 = right / -1 = left
        self.fleet_direction = 1