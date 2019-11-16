from enum import Enum
from ConvertMap import convert_address
from typing import List, Dict
from ConvertMap import convert
from ConvertMap import paint_map
import config


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

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Node:
    def __init__(self, coord: list, path=None, weight=0, visited: bool = False):
        if path is None:
            path = []

        self.path: list = path
        self.coord = coord
        self._visited = visited
        self.weight = weight
        # self.North = None
        # self.East = None
        # self.South = None
        # self.West = None

    # def __eq__(self, other):
    #     return self.lastDir == other.position

    def set_visited(self):
        self._visited = True

    def is_visited(self):
        return self._visited

    # def set_weight(self, weight: int):
    #     self.weight = weight


def add_bounds(node: Node, stack: list, node_grid, grid: List[List[bool]], width,
               height) -> None:
    """
    Warning! Coord and cardinal points are mixed up
    :param height: height of grid
    :param width: width of grid
    :param grid: Grid. 0 - blocked, 1 - open
    :return:
    """
    y = node.coord[0]
    x = node.coord[1]
    if y + 1 < height and grid[y + 1][x] and not node.is_visited():
        if not node_grid[y + 1][x]:
            new_dir = node.path.copy()
            new_dir.append(Direction.SOUTH)
            tmp = Node([y + 1, x], new_dir, node.weight + 1)
            node_grid[y + 1][x] = tmp
            stack.append(tmp)
        else:
            tmp: Node = node_grid[y + 1][x]
            if tmp.weight > node.weight + 1:
                tmp.weight = node.weight + 1
                tmp.path = node.path.copy()
                tmp.path.append(Direction.SOUTH)

    if y - 1 >= 0 and grid[y - 1][x] and not node.is_visited():
        if not node_grid[y - 1][x]:
            new_dir = node.path.copy()
            new_dir.append(Direction.NORTH)
            tmp = Node([y - 1, x], new_dir, node.weight + 1)
            node_grid[y - 1][x] = tmp
            stack.append(tmp)
        else:
            tmp: Node = node_grid[y - 1][x]
            if tmp.weight > node.weight + 1:
                tmp.weight = node.weight + 1
                tmp.path = node.path.copy()
                tmp.path.append(Direction.NORTH)

    if x + 1 < width and grid[y][x + 1] and not node.is_visited():
        if not node_grid[y][x + 1]:
            new_dir = node.path.copy()
            new_dir.append(Direction.WEST)
            tmp = Node([y, x + 1], new_dir, node.weight + 1)
            node_grid[y][x + 1] = tmp
            stack.append(tmp)

        else:
            tmp: Node = node_grid[y][x + 1]
            if tmp.weight > node.weight + 1:
                tmp.weight = node.weight + 1
                tmp.path = node.path.copy()
                tmp.path.append(Direction.WEST)

    if x - 1 >= 0 and grid[y][x - 1] and not node.is_visited():
        if not node_grid[y][x - 1]:
            new_dir = node.path.copy()
            new_dir.append(Direction.EAST)
            tmp = Node([y, x - 1], new_dir, node.weight + 1)
            node_grid[y][x - 1] = tmp
            stack.append(tmp)
        else:
            tmp: Node = node_grid[y][x - 1]
            if tmp.weight > node.weight + 1:
                tmp.weight = node.weight + 1
                tmp.path = node.path.copy()
                tmp.path.append(Direction.EAST)


def some_dijkstra(grid: List[List[bool]], pass_coord: Dict[int, int], height: int, width: int, car_coord: int):
    # grid with len
    res_node_list = {}
    node_grid = [[None for w in range(width)] for h in range(height)]
    double_pass_coord: Dict[int, List[int, int]] = {}
    for key1, item1 in pass_coord.items():
        double_pass_coord.update({key1: convert_address(item1, width)})

    queue = list()
    tmp1 = convert_address(car_coord, width)
    origNode = Node(tmp1)
    x = tmp1[0]
    y = tmp1[1]
    node_grid[x][y] = origNode
    queue.append(origNode)
    print(double_pass_coord)
    while queue:
        tmp: Node = queue.pop(0)
        add_bounds(tmp, queue, node_grid, grid, width, height)
        tmp.set_visited()

        if not double_pass_coord:
            break

        for key1, coord in double_pass_coord.items():
            if coord[0] == tmp.coord[0] and coord[1] == tmp.coord[1]:
                res_node_list.update({key1: tmp})
                double_pass_coord.pop(key1)
                break

    return res_node_list


if __name__ == '__main__':
    t = config.configA
    pass_arr = {}
    car_pos = []
    s = convert(t["grid"], t['width'])
    paint_map(s)
    for key, val in t["customers"].items():
        pass_arr.update({key: int(val['origin'])})
    for a in t["cars"].values():
        car_pos.append(int(a['position']))
    print(pass_arr)
    print(car_pos)

    for a in car_pos:
        nodes = some_dijkstra(s, pass_arr, t["height"], t["width"], a)
        for people_key, i in nodes.items():
            # row = []
            print(f"Client id - {people_key}")
            print("Weight")
            print(i.weight)
            print("Coords")
            print(i.coord)
            print("Path")
            print(i.path)
            # if some_t[i.coord[0]][i.coord[1]]:
            #     print(some_t[i.coord[0]][i.coord[1]].coord)
            # else:
            #     print(some_t[i.coord[0]][i.coord[1]])

        # for i in some_t:
        #     row = []
        #     for a in i:
        #         if a:
        #             sl = a.weight
        #         else:
        #             sl = -1
        #         row.append(sl)
        #     for rows in row:
        #         print(f"{rows:3}",end=" ")
        #     print("\n")
        print("-----------------------------------------------")

# s = [[]]
#
# for i in range(N):
#     pass
