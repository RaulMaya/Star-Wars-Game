import pandas as pd

class GameStats:
    """Statistics of the Game"""

    def __init__(self, sw_app_game):
        self.settings = sw_app_game.settings
        self.reset_stats()
        
        df = pd.read_csv('high-score.csv')

        # Starting Star Wars Game in an active state
        self.game_active =  False

        # High-score
        self.high_score = int(df['High-Score'][0])
        
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1


