#!/usr/local/bin/python3.3

# Any live cell with fewer than two live neighbours dies, as if caused by under-population.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overcrowding.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


def create_2x2_matrix(r, c):
    
    return [[0 for i in range(r)] for j in range(c)]

m = create_2x2_matrix(10, 10)


m[4][3] = 1


    

def wrap(cell, dimension):
    if (cell > dimension) or (cell < 0):
        return cell % dimension
    else:
        return cell


def check_neighbors(r, c, matrix):
    neighbors = []
    for row_i in range(len(matrix[0])): # each row in matrix
        for col_i in range(len(matrix[0][0])) : # each column
            for row_check in (-1, 0, 1):
                for col_check in (-1, 0, 1):
                    if matrix[wrap(r + row_check, len(matrix)][wrap(c + row_check)] == 1
                    
check_neighbors(m)
                    
        
