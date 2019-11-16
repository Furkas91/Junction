from munkres import Munkres, print_matrix
from random import randint
n, m = 4, 10
a = [[randint(1, 10) for j in range(m)] for i in range(n)]

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



