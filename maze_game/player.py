from BaseClasses import BasePlayer
from utils import *
import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

class Player(BasePlayer):
    def __init__(self, init_pos = (2, 2)):
        """
        #TODO init of positions.
        :init_pos: (row, col) initial position of player
        """
        super().__init__()
        self.row, self.col = init_pos
        logger.debug(f'Player object created.')

    def event_parse(self, event):
        mapping = {
            pygame.K_UP: UP,
            pygame.K_RIGHT: RIGHT,
            pygame.K_DOWN: DOWN,
            pygame.K_LEFT: LEFT,
        }
        if event.type == pygame.KEYDOWN:
            return mapping.get(event.key, None)

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
        logger.debug(f'Player moved: {move}')
        row = self.row
        col = self.col
        if move == UP:
            row -=1
        if move == RIGHT:
            col +=1
        if move == DOWN:
            row +=1
        if move == LEFT:
            col -=1
        if out_of_bound(env["dims"], (row, col)) or (row, col) in env["walls"]:
            return False
        self.row = row
        self.col = col
        return True


    def update(self, move, env):
        moved = self.move(move, env)
        logging.debug(f'{self.row, self.col}')
        return moved

    def draw(self, surface):
        row = self.row
        col = self.col
        pygame.draw.rect(surface, HEAD_BORDER,
                         pygame.Rect(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(surface, HEAD_COLOR,
                         pygame.Rect(col * BLOCK_SIZE + 4, row * BLOCK_SIZE + 4, BLOCK_SIZE - 8,
                                     BLOCK_SIZE - 8))
