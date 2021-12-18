import pygame

class SpaceShip:
    """A class to develop the space ship"""

    def __init__(self, alien_app_game):
        """Start the space ship and set the beginning point"""
        self.screen = alien_app_game.screen
        self.screen_rect = alien_app_game.screen.get_rect()

        # Load the space ship image and getting its rect
        self.image = pygame.image.load('images/px-mf.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement Flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position according to the movement flag status"""
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1
        elif self.moving_up:
            self.rect.y -= 1
        elif self.moving_down:
            self.rect.y += 1


    def blitme(self):
        """Drawing the ship at a specific location"""
        self.screen.blit(self.image, self.rect)
