#!/usr/local/bin/python3.3
from time import sleep
import sys

R = 10
C = 10

def create_matrix(r, c):
    return [[0 for i in range(r)] for j in range(c)]

matrix = create_matrix(R, C)
matrix[4][3] = 1
matrix[4][4] = 1
matrix[3][3] = 1
matrix[3][4] = 1
matrix[2][4] = 1


def wrap(r, c, R=R, C=C):
    return (r % R, c % C)

def count_neighbors(r, c, matrix=matrix, R=R, C=C):
    nneighbors = 0
    for row_check in (-1, 0, 1):
        for col_check in (-1, 0, 1):
            if (row_check == 0) and (col_check == 0):
                continue
            cell_row, cell_col = wrap((r + row_check), (c + col_check), R=R, C=C)
            if matrix[cell_row][cell_col]:
                nneighbors += 1
                #print "cell %s has neighbor: %s" % ((r, c), (cell_row, cell_col))
    return nneighbors


def generate_next(matrix):
    next = create_matrix(len(matrix), len(matrix[0]))
    for row in range(len(matrix)):
        for cell in range(len(matrix[0])):
            count = count_neighbors(row, cell, matrix)
            if matrix[row][cell]:
                if count < 2:
                    next[row][cell] = 0
                elif count in [2, 3]:
                    next[row][cell] = 1
                elif count < 3:
                    next[row][cell] = 0
            elif count == 3:
                next[row][cell] = 1
    return next
while 1:
    for line in matrix:
        print("%s \r" % line)

    sys.stdout.flush()
    sys.stdout.seek(0)
    
    matrix = generate_next(matrix)
    sleep(1)
                
            

# Any live cell with fewer than two live neighbours dies, as if caused by under-population.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overcrowding.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.                    
        
