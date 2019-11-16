# import numpy as np
# import skimage.graph
from enum import Enum


#
# T, F = True, False
# array = np.asarray(
#     [[T, F, F, T],
#      [T, T, F, T],
#      [F, T, T, F],
#      [T, T, T, T]])
# costs = np.where(array, 1, 1000)
# path, cost = skimage.graph.shortest_path(
#     costs, start=(0, 0), end=(3, 3), fully_connected=True)
#
# print(path)


def someDeicstra():
    # grid with len
    pass


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Node:
    def __init__(self, path: [Direction], weight=None, visited: bool = False):
        self._path = path
        self._visited = visited
        self._weight = weight
        self.North = None
        self.East = None
        self.South = None
        self.West = None

    def __eq__(self, other):
        return self.lastDir == other.position

    def set_visited(self):
        self._visited = True

    def get_path(self):
        return self._path

    def set_weight(self, weight: int):
        self._weight = weight


s = [[]]

for i in range(N):
    pass
