import argparse
from utils import *
import os

from maze_game import Game

parser = argparse.ArgumentParser(description="Game Master.")
parser.add_argument('--game', type=str, help="Python file that has game class.")
parser.add_argument('--player', type=str, help="Python file that has player class.")
args = parser.parse_args()
logging.debug(f'Game file: {args.game}  Player file: {args.player}')

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from constants import *

num_pass, num_fail = pygame.init()
logging.debug(f'Pygame modules initialized - success:{num_pass}  fail:{num_fail}')


screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill(WIN_COLOR)
pygame.display.set_caption(WIN_TITLE)
icon = pygame.image.load('./assets/images/icon.jpg')
pygame.display.set_icon(icon)
pygame.display.flip()


Game = import_class(module_name=args.game, class_name="Game")
Player = import_class(module_name=args.player, class_name="Player")
game = Game()
player = Player()
while game.state == RUNNING:
    player_move = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.state = QUIT
        player_move = player.event_parse(event)
    if player_move is not None:
        game.update(player_move)
        player.update(player_move, game.get_player_env())
    screen.fill(WIN_COLOR)
    game.draw(surface=screen)
    player.draw(surface=screen)
    pygame.display.flip()
pygame.display.quit()
