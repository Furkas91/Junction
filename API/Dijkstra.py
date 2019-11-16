import numpy as np
import skimage.graph
from enum import Enum

T, F = True, False
array = np.asarray(
    [[T, F, F, T],
     [T, T, F, T],
     [F, T, T, F],
     [T, T, T, T]])
costs = np.where(array, 1, 1000)
path, cost = skimage.graph.shortest_path(
    costs, start=(0, 0), end=(3, 3), fully_connected=True)

print(path)


def someDeicstra():
    # grid with len
    pass


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, lastDir=None, position=None):
        self.path = path
        self.lastDir = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.lastDir == other.position


s = [[]]

for i in range(N):
    pass
