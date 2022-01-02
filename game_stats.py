class GameStats:
    """Statistics of the Game"""

    def __init__(self, sw_app_game):
        self.settings = sw_app_game.settings
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit