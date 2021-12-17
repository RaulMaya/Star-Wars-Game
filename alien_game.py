import sys
import pygame
from settings import Settings

class AlienInvasion:
    """"Overall class to manage game assets and behavior"""

    def __init__(self):
        """Run the game, and develop necessary resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion II")

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redrawing the screen during each loop
            self.screen.fill(self.settings.bg_color)
            
            # Make the screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game prothotype, and run the game
    alien_app = AlienInvasion()
    alien_app.run_game()