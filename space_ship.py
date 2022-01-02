import pygame

class SpaceShip:
    """A class to develop the space ship"""

    def __init__(self, alien_app_game):
        """Start the space ship and set the beginning point"""
        self.screen = alien_app_game.screen
        self.settings = alien_app_game.settings
        self.screen_rect = alien_app_game.screen.get_rect()

        # Load the space ship image and getting its rect
        self.image = pygame.image.load('images/px-mf.bmp')
        self.image.set_colorkey((0,0,0)) # Hiding the background ((0,0,0)) => Black images background
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship horizontal and vertical position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


        # Movement Flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position according to the movement flag status"""
        # Updating ships x and y values
        """if self.moving_right:
            self.x += self.settings.space_ship_speed
        elif self.moving_left:
            self.x -= self.settings.space_ship_speed
        elif self.moving_up:
            self.y -= self.settings.space_ship_speed
        elif self.moving_down:
            self.y += self.settings.space_ship_speed"""

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.space_ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.space_ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.space_ship_speed  
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.space_ship_speed

        # Updating rect objects 
        self.rect.x = self.x
        self.rect.y = self.y


    def blitme(self):
        """Drawing the ship at a specific location"""
        self.screen.blit(self.image, self.rect)
