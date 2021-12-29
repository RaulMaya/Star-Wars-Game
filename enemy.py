import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):

    def __init__(self, alien_app_game):
        """Start the space ship and set the beginning point"""
        super().__init__()
        self.screen = alien_app_game.screen


        # Load the enemy ship image and getting its rect
        self.image = pygame.image.load('images/px-tiefighter.bmp')
        self.rect = self.image.get_rect()

        # Start each new enemy at the bottom center of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store a decimal value for the enemy horizontal and vertical position
        self.x = float(self.rect.x)
    