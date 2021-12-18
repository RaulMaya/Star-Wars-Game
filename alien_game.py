import sys
import pygame
from settings import Settings
from space_ship import SpaceShip

class AlienInvasion:
    """"Overall class to manage game assets and behavior"""

    def __init__(self):
        """Run the game, and develop necessary resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Empire Strikes Back")

        self.space_ship = SpaceShip(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()
            self.space_ship.update()

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


    def _update_screen(self):
            # Redrawing the screen during each loop
            self.screen.fill(self.settings.bg_color)
            self.space_ship.blitme()


            # Make the screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game prothotype, and run the game
    alien_app = AlienInvasion()
    alien_app.run_game()