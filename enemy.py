import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):

    def __init__(self, alien_app_game):
        """Start the space ship and set the beginning point"""
        super().__init__()
        self.screen = alien_app_game.screen
        self.settings = alien_app_game.settings


        # Load the enemy ship image and getting its rect
        self.image = pygame.image.load('images/px-tiefighter.bmp')
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

        # Start each new enemy at the bottom center of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store a decimal value for the enemy horizontal and vertical position
        self.x = float(self.rect.x)

    def check_edges(self):
        # Return Ture if alien is at the edge pf the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


    def update(self):
        """Move Enemy to the Right"""
        self.x += (self.settings.enemy_speed * self.settings.fleet_direction)
        self.rect.x =self.x



