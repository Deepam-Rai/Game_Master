from utils import *
from constants import *


class BaseGame:
    def __init__(self, state=RUNNING):
        self.state = state

    def game_over(self):
        logging.debug(f'GAME OVER')
        return

    def update(self, *args, **kwargs):
        """
        Updates the state of game according to the parameters provided.
        :param kwargs:
        :return: New state
        """
        return self.state

    def get_player_env(self, *args, **kwargs):
        """
        Returns the environment details of the specified player.
        :param args:
        :param kwargs:
        :return:
        """
        return

    def draw(self, surface):
        """
        Draws the game on the surface.
        :param surface:
        :return:
        """
        return
