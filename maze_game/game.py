import random

import pygame
from BaseClasses import BaseGame
from constants import *
from .constants import *
from .wilson import get_wilson_walls
import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


class Game(BaseGame):
    def __init__(self, state=RUNNING, dims=[MAZE_ROWS, MAZE_COLS]):
        super().__init__()
        self.state = state
        self.dims = dims
        self.walls = get_wilson_walls(self.dims)
        self.end_point = self.get_end_point()
        self.tick = CLOCK_TICK
        logging.debug("Game object created")

    def get_player_env(self):
        payload = {
            "dims": self.dims,
            "walls": self.walls
        }
        return payload

    def get_game_init_det(self):
        """
        Returns a random start point in the maze.
        :return: {
                    "start_point": (,) Coordinate tuple
                 }
        """
        start_point = tuple(random.randint(0, i-1) for i in self.dims)
        while start_point in self.walls or start_point == self.end_point:
            start_point = tuple(random.randint(0, i-1) for i in self.dims)
        payload = {
            "start_point": start_point
        }
        return payload

    def get_end_point(self):
        """
        :return: Ending point in the maze for the game.
        """
        end_point = tuple(random.randint(0, i - 1) for i in self.dims)
        while end_point in self.walls:
            end_point = tuple(random.randint(0, i - 1) for i in self.dims)
        return end_point

    def update(self, player_checks):
        """
        Checks game over
        :return:
        """
        player_pos = player_checks["position"]
        if player_pos == self.end_point:
            self.state = WON
        return

    def draw(self, surface):
        for wall in self.walls:
            pygame.draw.rect(surface, WALL_BORDER,
                             pygame.Rect(wall[1] * BLOCK_SIZE, wall[0] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, WALL_COLOR,
                             pygame.Rect(wall[1] * BLOCK_SIZE + 4, wall[0] * BLOCK_SIZE + 4, BLOCK_SIZE - 8,
                                         BLOCK_SIZE - 8))
        pygame.draw.rect(surface, END_BORDER,
                         pygame.Rect(self.end_point[1] * BLOCK_SIZE, self.end_point[0] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(surface, END_COLOR,
                         pygame.Rect(self.end_point[1] * BLOCK_SIZE + 4, self.end_point[0] * BLOCK_SIZE + 4, BLOCK_SIZE - 8,
                                     BLOCK_SIZE - 8))
        return
