import sys
import pygame
from settings import Settings
from space_ship import SpaceShip
from bullets import Bullets

class AlienInvasion:
    """"Overall class to manage game assets and behavior"""

    def __init__(self):
        """Run the game, and develop necessary resources"""
        pygame.init()
        self.settings = Settings()

        # Full Screen
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        # Custom Screen
        # self.screen = pygame.display.set_mode(
            # (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Empire Strikes Back")

        self.space_ship = SpaceShip(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.space_ship.update()
            self.bullets.update()
            self._update_screen()
            
    def _check_events(self):
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Event handler that responds to keypresses"""
        if event.key ==pygame.K_RIGHT:
            # Move the ship to the right.
            self.space_ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left.
            self.space_ship.moving_left = True
        elif event.key == pygame.K_UP:
            # Move the ship up.
            self.space_ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            # Move the ship down.
            self.space_ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup_events(self, event):
        """Event handler that responds to keypresses"""
        if event.key ==pygame.K_RIGHT:
            # Blocking the movement of the ship to the right.
            self.space_ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Blocking the movement of the ship to the left.
            self.space_ship.moving_left = False
        elif event.key == pygame.K_UP:
            # Blocking the movement the ship up.
            self.space_ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            # Blocking the movement the ship down.
            self.space_ship.moving_down = False
    
    def _fire_bullets(self):
        """Creating a new bullet"""
        new_bullet = Bullets(self)
        self.bullets.add(new_bullet)


    def _update_screen(self):
            # Redrawing the screen during each loop
            self.screen.fill(self.settings.bg_color)
            self.space_ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullets()


            # Make the screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game prothotype, and run the game
    alien_app = AlienInvasion()
    alien_app.run_game()