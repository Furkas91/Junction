from munkres import Munkres, print_matrix
from random import randint
from Apathfind import astar
import ConvertMap as cm
import config

def make_matrix(configM):
    grid = configM('grid')
    width = configM('width')
    cars = configM('cars').values()
    customers = configM('customers').values()
    new = cm.convert(grid, width)
    cm.paint_map(new)
    customers = []
    for customer in configM['customers'].values():
        pr = [customer]
        s = int(customer['origin'])
        e = int(customer['destination'])
        start = cm.convert_address(s, width)
        end = cm.convert_address(e, width)
        #print(start, end)
        path = astar(new, start, end)
        #print(path)
        pr.append(path)
        customers.append(pr)
    print(customers)

def hung():
    n, m = 4, 10
    a = [[randint(1, 10) for j in range(m)] for i in range(n)]
    # Если исполнить нельзя - DISABLED
    matrix = a

    # matrix = [[5, 9, 1, 12, 54, 75, 3],
    #           [10, 3, 2, 3, 7, 23, 12],
    #           [8, 7, 4, 12, 12, 12, 9],
    #           [19, 17, 13, 10, 9, 8, 7]]

    m = Munkres()

    m.pad_matrix(matrix, 0)

    indexes = m.compute(matrix)

    print_matrix(matrix, msg='Lowest cost through this matrix')
    total = 0
    for row, column in indexes:
        value = matrix[row][column]
        total+= value
        print(f'({row}, {column}) -> {value}')
    print(f'total cost: {total}')

if __name__ == '__main__':
    make_matrix(config.configB)

