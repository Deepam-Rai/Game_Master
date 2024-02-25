import pygame
from BaseClasses import BasePlayer
from .utils import *
from .constants import *
import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


class Player(BasePlayer):
    def __init__(self, game_init_det):
        """
        #TODO init of positions.
        :arg game_init_details: Provides "start_point" of the player in the maze.
        """
        super().__init__()
        self.row, self.col = game_init_det["start_point"]
        self.moving = STILL
        logger.debug(f'Player object created.')

    def event_parse(self, event):
        dir_map = {
            pygame.K_UP: UP,
            pygame.K_RIGHT: RIGHT,
            pygame.K_DOWN: DOWN,
            pygame.K_LEFT: LEFT,
        }
        if event.type == pygame.KEYDOWN:
            return dir_map.get(event.key, None)
        if event.type == pygame.KEYUP:
            return STILL

    def move(self, move, env):
        """
        Updates the position of the player.
        :param move: the move that player makes
        :param env:
            {
                "dims" : [dim1, dim2],
                "walls": [(,),(,),...] # maze walls as tuple list
            }
        :return: True if change in position else false
        """
        self.moving = move if move in [UP, RIGHT, DOWN, LEFT, STILL] else self.moving
        row = self.row
        col = self.col
        if self.moving == UP:
            row -=1
        if self.moving == RIGHT:
            col +=1
        if self.moving == DOWN:
            row +=1
        if self.moving == LEFT:
            col -=1
        if out_of_bound(env["dims"], (row, col)) or (row, col) in env["walls"]:
            return False
        self.row = row
        self.col = col
        return True

    def update(self, move, env):
        moved = self.move(move, env)
        return moved

    def get_player_checks(self):
        """
        For the game to check if its game over.
        :return: {
                    "position": (,) players curent position.
                 }
        """
        payload = {
            "position": (self.row, self.col)
        }
        return payload

    def draw(self, surface):
        row = self.row
        col = self.col
        pygame.draw.rect(surface, PLAYER_BORDER,
                         pygame.Rect(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(surface, PLAYER_COLOR,
                         pygame.Rect(col * BLOCK_SIZE + 4, row * BLOCK_SIZE + 4, BLOCK_SIZE - 8,
                                     BLOCK_SIZE - 8))
