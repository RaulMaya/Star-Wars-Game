import pygame.font

class Scoreboard:
    """ A class to report scoring information."""

    def __init__(self, sw_app_game):
        """Initiate Score Board"""
        self.screen = sw_app_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sw_app_game.settings
        self.stats = sw_app_game.stats

        # Font Settings For Scoring Information
        self.text_color = (255, 215, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score board
        self.prep_score()

    def prep_score(self):
        """Turning the score number into the score board"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.screen_rect.top = 20

    def show_score(self):
        """Draw the score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)