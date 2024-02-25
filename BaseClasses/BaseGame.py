from utils import *
from constants import *


class BaseGame:
    def __init__(self, state=RUNNING, tick=20):
        self.state = state
        self.tick = tick

    def update(self, *args, player_checks, **kwargs):
        """
        Updates the state of game according to the parameters provided.
        :arg player_checks: Necessary details provided by player to check if player is in special position(game over, etc).
        :param kwargs:
        :return: New state
        """
        return self.state

    def game_over(self):
        logging.debug(f'GAME OVER')
        return

    def get_player_env(self, *args, **kwargs):
        """
        Returns the environment details of the specified player.
        :param args:
        :param kwargs:
        :return:
        """
        return

    def get_game_init_det(self, *args, **kwargs):
        """
        Returns the neccesary details that game must provide to Player object when player is created.
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
