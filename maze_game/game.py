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
        self.state = state
        self.dims = dims
        self.walls = get_wilson_walls(self.dims)
        logging.debug("Game object created")

    def get_player_env(self):
        payload = {
            "dims": self.dims,
            "walls": self.walls
        }
        return payload

    def draw(self, surface):
        for wall in self.walls:
            pygame.draw.rect(surface, WALL_BORDER,
                             pygame.Rect(wall[1] * BLOCK_SIZE, wall[0] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, WALL_COLOR,
                             pygame.Rect(wall[1] * BLOCK_SIZE + 4, wall[0] * BLOCK_SIZE + 4, BLOCK_SIZE - 8,
                                         BLOCK_SIZE - 8))
        return
