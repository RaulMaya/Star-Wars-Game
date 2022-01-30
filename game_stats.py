class GameStats:
    """Statistics of the Game"""

    def __init__(self, sw_app_game):
        self.settings = sw_app_game.settings
        self.reset_stats()

        # Starting Star Wars Game in an active state
        self.game_active =  False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0


