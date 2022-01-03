import pygame
from pygame.sprite import Sprite
import random

class Enemy_Bullets(Sprite):
    """Class to manage the ammo"""

    def __init__(self, sw_app_game):
        """Create bullets at the space ships position"""
        super().__init__()
        self.screen =sw_app_game.screen
        self.settings = sw_app_game.settings
        self.color = self.settings.enemy_bullet_color 

        # Create the ammunition rect at (0,0) and then establish the correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        enemy =  random.choice(sw_app_game.enemies.sprites())
        self.rect.midbottom = enemy.rect.midbottom

        # Bullets position as decimal value
        self.y = float(self.rect.y)
    

    def update(self):
        """Moving the bullet downwards"""
        # Update the decimal position
        self.y += self.settings.enemy_bullet_speed
        # Update of rect position
        self.rect.y = self.y


    def draw_enemy_bullets(self):
        """Drawing the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

