import ConvertMap as cm
from config import configA
from client import CarDirection

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)
    flag = 0
    # Loop until you find the end
    while len(open_list) > 0:
        if maze[end_node.position[0]][end_node.position[1]] != True or maze[start_node.position[0]][start_node.position[1]] != True:
            print("VERY FUCKING STUPID CUSTOMER")
            break

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        # --
        #print(end_node.position, 'BLIYAAAA')
        #print(current_node.position, 'closed')
        # --

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            path = path[::-1]
            #print(path[1][0])
            new_path = []
            for i in range(len(path) - 1):
                direct = [0,0]
                #print(direct[0])
                direct[0] = path[i + 1][0] - path[i][0]
                direct[1] = path[i + 1][1] - path[i][1]
                if direct == [1, 0]:
                    new_path.append(CarDirection.south)
                elif direct == [-1, 0]:
                    new_path.append(CarDirection.north)
                elif direct == [0, 1]:
                    new_path.append(CarDirection.east)
                elif direct == [0, -1]:
                    new_path.append(CarDirection.west)

            return len(new_path), new_path  # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != True:
                #print(node_position, 'continue pizda')
                # if node_position == end_node.position:
                #     flag = 1
                #     break
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            #if new_node in children:
                #print("ON PIDOR")
            # Append
            children.append(new_node)
            # ________________________
            #print(new_node.position, 'children')
            # _________________________
        # Loop through children
        for child in children:

            # Child is on the closed list
            #for closed_child in closed_list:
            if child in closed_list:
                #print(child.position, "child closed")
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                        (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
            # --
            #print(child.position, 'open')
            # --


def main():
    maze = [[False, False, False, False, True, False, False, False, False, False],
            [False, False, False, False, True, False, False, False, False, False],
            [False, False, False, False, True, False, False, False, False, False],
            [False, False, False, False, True, False, False, False, False, False],
            [False, False, False, False, True, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, True, False, False, False, False, False],
            [False, False, False, False, True, False, False, False, False, False],
            [False, False, False, False, True, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False]]

# start = cm.convert_address(300, 32)
# end = cm.convert_address(320, 32)
    grid = configA['grid']
    width = configA['width']
    for customer in configA['customers'].values():
        s = int(customer['origin'])
        e = int(customer['destination'])
        start = cm.convert_address(s, width)
        end = cm.convert_address(e, width)
        print(start, end)
        new = cm.convert(grid, width)
        cm.paint_map(new)
        path = astar(new, start, end)
        print(path)

# for customer in configA['cars'].values():
#     s = int(customer['position'])
#     e = int(customer['position'])
#     start = cm.convert_address(s, width)
#     end = cm.convert_address(e, width)
#     print(start, end, new[start[0]][start[1]])
#     new = cm.convert(grid, width)
#     cm.paint_map(new)
# start = cm.convert_address(0, 32)
# end = cm.convert_address(0, 32)
# start = cm.convert_address(620, 32)
# end = cm.convert_address(183, 32)
# start = (0, 31)
# end = (0, 23)


# start = cm.convert_address(3, 32)
# end = cm.convert_address(0, 32)
# print(start, end)
# new = cm.convert(grid, 32)


# cm.paint_map(new)
# path = astar(new, start, end)
# print(path)

if __name__ == '__main__':
    main()
