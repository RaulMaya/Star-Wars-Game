class Settings:
    """Class to store all settings from the Alien Invasion Game"""

    def __init__(self):
        """Execute game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (136,0,21)

        # Space ship settings
        self.space_ship_speed = 0.75