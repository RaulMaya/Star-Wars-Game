import pygame

class SpaceShip:
    """A class to develop the space ship"""

    def __init__(self, alien_app_game):
        """Start the space ship and set the beginning point"""
        self.screen = alien_app_game.screen
        self.screen_rect = alien_app_game.screen.get_rect()

        # Load the space ship image and getting its rect
        self.image = pygame.image.load('images/mf.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Drawing the ship at a specific location"""
        self.screen.blit(self.image, self.rect)