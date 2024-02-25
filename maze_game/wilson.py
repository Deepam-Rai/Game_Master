from .constants import *
import random
import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


def get_rand_loc(dims):
    return tuple(random.randint(0, dim_bound-1) for dim_bound in dims)


def get_excluded_rand_loc(dims, to_exclude):
    if len(to_exclude) >= get_num_cells(dims):
        return None
    rand_loc = get_rand_loc(dims)
    while rand_loc in to_exclude:
        rand_loc = get_rand_loc(dims)
    return rand_loc


def get_num_cells(dims):
    num = dims[0]
    for dim_bound in dims[1:]:
        num = num * dim_bound
    return num


def is_plus_neighbor(a, b):
    """ Example:
    1 2 3
    4 5 6
    7 8 9
    Here, 2,4,6,8 are plus neighbors of 5.
    :param a: location of cell
    :param b: location of another cell
    :return: True if they are plus neighbors
    """
    diff = sum([abs(a_coord - b_coord) for a_coord, b_coord in list(zip(a, b))])
    return True if diff == 1 else False


def get_neighbors(current_loc, dims, only_plus=True):
    neighbors = []
    for i in range(len(dims)):
        if current_loc[i] - 1 >= LOWER_BOUND:
            new_neighbor = list(current_loc)
            new_neighbor[i] -= 1
            neighbors += [tuple(new_neighbor)]
        if current_loc[i] + 1 < dims[i]:
            new_neighbor = list(current_loc)
            new_neighbor[i] += 1
            neighbors += [tuple(new_neighbor)]
    if only_plus:
        plus_neighbors = [ x for x in neighbors if is_plus_neighbor(current_loc, x)]
        neighbors = plus_neighbors
    return tuple(neighbors)


def get_new_walk(dims, included):
    """
    Gets new random walk, that starts on any random location except "included" locations
     and ends on one of the "included" location.
    :param dims: [x_dim, y_dim] : dimension of maze
    :param included: [loc1, loc2,...] : locations that should only be at the end of the returned walk.
    :return: wilson walk. e.g., [loc1, loc2, ..., locn] where "locn" is and the only location from "included".
    """
    start_loc = get_excluded_rand_loc(dims, included)
    if start_loc is None:
        return None
    current_loc = start_loc
    new_walk = [start_loc]
    while current_loc not in included:
        neighbors = get_neighbors(current_loc, dims)
        if all(neighbor in new_walk for neighbor in neighbors):
            return get_new_walk(dims, included)
        new_loc = random.choice(list(set(neighbors) - set(new_walk)))
        new_walk += [new_loc]
        current_loc = new_loc
    return new_walk


def wilson_algo(dims):
    start_loc = get_rand_loc(dims)
    wilson_walks = [
        [start_loc]
    ]
    done = set([start_loc])
    while len(done) < get_num_cells(dims):
        new_walk = get_new_walk(dims, included=done)
        wilson_walks = wilson_walks + [new_walk]
        done = done.union(set(new_walk))
    return wilson_walks


def get_walled_cells(dims):
    # top-left is (0,0)
    # need to generalize for >2 dim
    construct = [[WALL for col in range(dims[1]*2 + 1)] for row in range(dims[0]*2 +1)]
    for row in range(1, dims[0]*2+1, 2):
        for col in range(1, dims[1]*2+1, 2):
            construct[row][col] = CELL
    return construct


def get_rel_dir(x, respect_to):
    to_return = []
    if x[0] < respect_to[0]:
        to_return.append(UP)
    if x[1] > respect_to[1]:
        to_return.append(RIGHT)
    if x[0] > respect_to[0]:
        to_return.append(DOWN)
    if x[1] < respect_to[1]:
        to_return.append(LEFT)
    if len(to_return) == 0:
        to_return.append(COINCI)
    return to_return


def remove_wall(maze, cell, direction, to_put=CELL):
    row, col = cell
    row = row*2 + 1
    col = col*2 + 1
    if direction == UP:
        row -= 1
    if direction == DOWN:
        row += 1
    if direction == RIGHT:
        col += 1
    if direction == LEFT:
        col -= 1
    maze[row][col] = to_put
    return maze


def remove_walls(maze, wilson_walks):
    for walk in wilson_walks:
        for a,b in list(zip(walk[:-1], walk[1:])):
            direction = get_rel_dir(x=a, respect_to=b)[0]
            maze = remove_wall(maze, b, direction)
    return maze

def bremove_walls(maze, wilson_tuples):
    for cell, neighbors in wilson_tuples.items():
        print(cell, neighbors)
        for neighor in neighbors:
            direction = get_rel_dir(x=neighor, respect_to=cell)[0]
            maze = remove_wall(maze, cell, direction)
    return maze


def create_wilson_maze(dims, return_wilson=False):
    wilson_walks = wilson_algo(dims)
    print(wilson_walks)
    maze = get_walled_cells(dims)
    maze = remove_walls(maze, wilson_walks)
    if return_wilson:
        return maze, wilson_walks
    return maze


def get_walls(maze):
    """
    :param maze: maze as 2D list.
    :return: [wall1, wall2,...,(row,col)]
    """
    walls = []
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == WALL:
                walls.append((row, col))
    return walls


def get_wilson_walls(dims):
    """
    Returns coordinates of walls of maze created using wilson algorithm.
    :param dims:
    :return: [(,),(,)...] tuples of walls coordinates as list.
    """
    #TODO: remove need of halving the dims
    wilson_walks = wilson_algo([(dims[0]-1)//2, (dims[1]-1)//2])
    maze = get_walled_cells(dims)
    maze = remove_walls(maze, wilson_walks)
    return get_walls(maze)


def visualize(maze):
    for row in maze:
        for unit in row:
            print(PRINTS[unit], end="")
        print()


def check_connected_wilson(wilson_tuples):
    components = [ set([k]).union(set(v)) for k, v in wilson_tuples.items()]
    print(components)


def dcheck_connected_wilson(wilson_tuples):
    for k, v in wilson_tuples.items():
        if len(v) > 0:
            heads = [k]
            break
    components = set()
    for h in heads:
        if h not in components:
            components.add(h)
            heads += list(wilson_tuples[h])
    diff = set(wilson_tuples.keys()) - components
    if len(diff) == 0:
        return True, diff
    else:
        return False, diff


def check_connected(maze):
    start_cell = [-1, -1]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == CELL:
                start_cell = (i, j)
                break
        else:
            continue
        break
    else:
        return None, maze
    component = [start_cell]
    for x in component:
        maze[x[0]][x[1]] = WALL
        if x[0]-1 >= 0 and maze[x[0]-1][x[1]] == CELL:
            component += [(x[0]-1, x[1])]
        if x[0]+1 < len(maze) and maze[x[0]+1][x[1]] == CELL:
            component += [(x[0]+1, x[1])]
        if x[1]-1 >= 0 and maze[x[0]][x[1]-1] == CELL:
            component += [(x[0], x[1]-1)]
        if x[1]+1 < len(maze[0]) and maze[x[0]][x[1]+1] == CELL:
            component += [(x[0], x[1]+1)]
    if CELL in sum(maze, []):
        return False, maze
    return True, maze


if __name__ == "__main__":
    dims = [12,50]
    # dims = [4, 4]
    maze, wilson_walks = create_wilson_maze(dims, return_wilson=True)
    # logging.debug(f'Final MAZE:\n{maze}')
    visualize(maze)
    connected, components = check_connected(maze)
    print(f'maze check: {connected}')
    # visualize(components)
