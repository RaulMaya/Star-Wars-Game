import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    """Class to manage the ammo"""

    def __init__(self, alien_app_game):
        """Create bullets at the space ships position"""
        super().__init__()
        self.screen =alien_app_game.screen
        self.settings = alien_app_game.settings
        self.color = self.settings.bullet_color

        # Create the ammunition rect at (0,0) and then establish the correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = alien_app_game.ship.rect.midtop

        # Bullets position as decimal value
        self.y = float(self.rect.y)

        
