import pygame
from constants import *
import logging
import sys
import importlib

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


def import_class(module_name, class_name):
    try:
        module = importlib.import_module(module_name)
        class_ = getattr(module, class_name)
        return class_
    except (ImportError, AttributeError):
        logging.error(f"Class {class_name} not found in module {module_name}.")


def out_of_bound(dims, pos):
    row = pos[0]
    col = pos[1]
    if row < 0 or col < 0 or row >=dims[0] or col > dims[1]:
        return True
    return False


def draw(surface, walls, player):
    # body
    for wall in walls:
        pygame.draw.rect(surface, WALL_BORDER, pygame.Rect(wall[0]*BLOCK_SIZE, wall[1]*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(surface, WALL_COLOR, pygame.Rect(wall[0]*BLOCK_SIZE+4, wall[1]*BLOCK_SIZE+4, BLOCK_SIZE - 8, BLOCK_SIZE - 8))
    # Head
    pygame.draw.rect(surface, HEAD_BORDER, pygame.Rect(player[0]*BLOCK_SIZE, player[1]*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(surface, HEAD_COLOR, pygame.Rect(player[0]*BLOCK_SIZE+4, player[1]*BLOCK_SIZE+4, BLOCK_SIZE - 8, BLOCK_SIZE - 8))
