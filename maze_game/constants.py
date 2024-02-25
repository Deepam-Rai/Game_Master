# maze constants
MAZE_ROWS = 31
MAZE_COLS = 31
CELL = 0
WALL = 1
FILLED = WALL
EMPTY = CELL

PRINTS = {
    WALL: "#",
    CELL: " "
}

LOWER_BOUND = 0

# Directions
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4
COINCI = 0

# draw constants
WALL_COLOR = '#936a2e'
WALL_BORDER = '#765119'
PLAYER_COLOR = (100, 80, 235)
PLAYER_BORDER = (102, 0, 204)

# game constants
BLOCK_SIZE = 20
WIN_HEIGHT = MAZE_ROWS * BLOCK_SIZE
WIN_WIDTH = MAZE_COLS * BLOCK_SIZE
WIN_COLOR = '#38a922' # '#808080'
WIN_TITLE = 'Maze Solver'
WIN_ICON = 'maze_game/assets/images/icon.jpg'
