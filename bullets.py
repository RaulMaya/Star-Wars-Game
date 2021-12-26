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
        self.rect.midtop = alien_app_game.space_ship.rect.midtop

        # Bullets position as decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Moving the bullet upwards"""
        # Update the decimal position
        self.y -= self.settings.bullet_speed
        # Update of rect position
        self.rect.y = self.y

    def draw_bullets(self):
        """Drawing the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

