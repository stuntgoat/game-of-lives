#!/usr/local/bin/python3.3
from time import sleep
import sys

R = 45
C = 45

def create_matrix(r, c):
    return [[0 for i in range(r)] for j in range(c)]

matrix = create_matrix(R, C)

matrix[0][2] = 1
matrix[1][0] = 1
matrix[1][2] = 1
matrix[2][1] = 1
matrix[2][2] = 1
matrix[11][2] = 1
matrix[12][0] = 1
matrix[12][2] = 1
matrix[13][1] = 1
matrix[13][2] = 1
matrix[7][5] = 1
matrix[8][5] = 1
matrix[8][7] = 1
matrix[9][5] = 1
matrix[9][6] = 1
matrix[33][2] = 1
matrix[33][3] = 1
matrix[33][4] = 1
matrix[32][4] = 1
matrix[33][3] = 1
matrix[15][14] = 1
matrix[14][14] = 1
matrix[13][14] = 1
matrix[12][14] = 1
matrix[11][14] = 1
matrix[10][14] = 1
matrix[24][2] = 1
matrix[24][3] = 1
matrix[24][4] = 1
matrix[23][4] = 1
matrix[22][3] = 1
matrix[24][2] = 1
matrix[24][3] = 1
matrix[24][4] = 1
matrix[23][4] = 1
matrix[22][3] = 1
matrix[41][2] = 1
matrix[41][3] = 1
matrix[41][4] = 1
matrix[40][4] = 1
matrix[39][3] = 1







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
count = 0
while 1:

    for line in matrix:
        
        sys.stdout.write("%s \n" % line)
#        sys.stdout.write("\r" % line)
        sys.stdout.seek(0)
        #sys.stdout.flush()
    sys.stdout.write('%d \n' % count)
    
    sys.stdout.seek(0)
    
    matrix = generate_next(matrix)
    sleep(.01)
    count += 1
    
            

# Any live cell with fewer than two live neighbours dies, as if caused by under-population.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overcrowding.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.                    
        
