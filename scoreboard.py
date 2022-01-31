import pygame.font
from pygame.sprite import Group
from life_ship import LifeShip

class Scoreboard:
    """ A class to report scoring information."""

    def __init__(self, sw_app_game):
        """Initiate Score Board"""
        self.sw_app_game = sw_app_game
        self.screen = sw_app_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sw_app_game.settings
        self.stats = sw_app_game.stats

        # Font Settings For Scoring Information
        self.text_color = (255, 215, 0)
        self.font = pygame.font.SysFont(None, 35)

        # Prepare the initial score board and high score
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_space_ships()

    def prep_score(self):
        """Turning the score number into the score board"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.screen_rect.top = 20

    def show_score(self):
        """Draw the ships, score, the high score and level to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.space_ships.draw(self.screen)

    def prep_high_score(self):
        """Turn the highscore into rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Centering the High Score
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check if there is a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Turn the level into rendered image"""
        level_str = "Wave: {}".format(str(self.stats.level))
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Position of the Level
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_space_ships(self):
        """Show how many space ships are left"""
        self.space_ships = Group()
        for ship_number in range(self.stats.ships_left):
            space_ship = LifeShip(self.sw_app_game)
            space_ship.rect.x = 10 + ship_number * space_ship.rect.width
            space_ship.rect.y = 10
            self.space_ships.add(space_ship)
