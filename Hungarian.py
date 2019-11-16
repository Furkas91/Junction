from munkres import Munkres, print_matrix
from random import randint
from Apathfind import astar
from Dijkstra import some_dijkstra
import ConvertMap as cm
import config

def make_matrix(configM):
    grid = configM['grid']
    width = configM['width']
    height = configM['height']
    cars = configM['cars'].values()
    customers = configM['customers'].values()
    #print(customers)
    origins = []
    for i in customers:
        origins.append(i['origin'])
    new = cm.convert(grid, width)
    cm.paint_map(new)
    custom = []
    custom_id=0
    car_id=0
    for customer in configM['customers'].values():
        pr = [custom_id]
        s = int(customer['origin'])
        e = int(customer['destination'])
        start = cm.convert_address(s, width)
        end = cm.convert_address(e, width)
        #print(start, end)
        path = astar(new, start, end)
        #print(path)
        pr.append(path)
        custom.append(pr)
        custom_id = custom_id + 1
    #print(customers)
    cars=[]
    for car in configM['cars'].values():
        nodes = some_dijkstra(new, origins, height, width, car['position'])
        cars.append((car_id, nodes))
        car_id+=1
    #print(cars)
    matrix=[]
    for car in cars:
        row = []
        for pas in custom:
            row.append(car[1][pas[0]].weight+pas[1][1])
        matrix.append(row)
    return matrix


def hung(matrix):
    #n, m = 4, 10
    #a = [[randint(1, 10) for j in range(m)] for i in range(n)]
    ## Если исполнить нельзя - DISABLED
    #matrix = a

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
    matrix = make_matrix(config.configA)
    print(matrix)
    hung(matrix)

