import argparse
from utils import *
import os

parser = argparse.ArgumentParser(description="Game Master. Controls the game loop. Can take different games and players as form of python modules. Base classes for Game and Player are defined inside 'BaseClasses' module.")
parser.add_argument('--game', type=str, help="Python module that has 'Game' class. Should also contain `win_configs.py` file that defines constants WIN_HEIGHT, WIN_WIDTH, WIN_TITLE, WIN_COLOR, WIN_ICON.")
parser.add_argument('--player', type=str, help="Python module that has 'Player' class.")
args = parser.parse_args()
logging.debug(f'Game module: {args.game}  Player module: {args.player}')

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from constants import *

num_pass, num_fail = pygame.init()
logging.debug(f'Pygame modules initialized - success:{num_pass}  fail:{num_fail}')

win_configs = import_constants(module_name=args.game)
screen = pygame.display.set_mode((win_configs["WIN_WIDTH"], win_configs["WIN_HEIGHT"]))
screen.fill(win_configs["WIN_COLOR"])
pygame.display.set_caption(win_configs["WIN_TITLE"])
icon = pygame.image.load(win_configs["WIN_ICON"])
pygame.display.set_icon(icon)
pygame.display.flip()

clock = pygame.time.Clock()
Game = import_class(module_name=args.game, class_name="Game")
Player = import_class(module_name=args.player, class_name="Player")
game = Game()
player = Player(game_init_det = game.get_game_init_det())
while game.state == RUNNING:
    player_move = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.state = QUIT
        player_move = player.event_parse(event)
    player.update(player_move, game.get_player_env())
    game.update(player_checks=player.get_player_checks())
    screen.fill(win_configs["WIN_COLOR"])
    game.draw(surface=screen)
    player.draw(surface=screen)
    pygame.display.flip()
    clock.tick(game.tick)
logger.debug(f'Game state: {game.state}')
pygame.display.quit()
