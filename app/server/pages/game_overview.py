from .BasePage import BasePage

class GameOverview(BasePage):
    def __init__(self):
        super().__init__(name="GameOverview", path="/game_overview")