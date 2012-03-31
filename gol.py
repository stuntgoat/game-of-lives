#!/usr/local/bin/python3.3
from time import sleep
import sys

R = 45
C = 45

def create_matrix(r, c):
    return [[' ' for i in range(r)] for j in range(c)]
matrix = create_matrix(R, C)

matrix[0][2]   ='O'
matrix[1][0]   ='O'
matrix[1][2]   ='O'
matrix[2][1]   ='O'
matrix[2][2]   ='O'
matrix[11][2]  ='X'
matrix[12][0]  ='X'
matrix[12][2]  ='X'
matrix[13][1]  ='X'
matrix[13][2]  ='X'
matrix[7][5]   ='X'
matrix[8][5]   ='X'
matrix[8][7]   ='X'
matrix[9][5]   ='X'
matrix[9][6]   ='X'
matrix[33][2]  ='X'
matrix[33][3]  ='X'
matrix[33][4]  ='X'
matrix[32][4]  ='X'
matrix[33][3]  ='X'
matrix[15][14] ='X'
matrix[14][14] ='X'
matrix[13][14] ='X'
matrix[12][14] ='X'
matrix[11][14] ='X'
matrix[10][14] ='X'
matrix[24][2]  ='O'
matrix[24][3]  ='O'
matrix[24][4]  ='O'
matrix[23][4]  ='O'
matrix[22][3]  ='O'
matrix[24][2]  ='O'
matrix[24][3]  ='O'
matrix[24][4]  ='O'
matrix[23][4]  ='O'
matrix[22][3]  ='O'
matrix[41][2]  ='O'
matrix[41][3]  ='O'
matrix[41][4]  ='O'
matrix[40][4]  ='O'
matrix[39][3]  ='O'
matrix[41][20]  ='X'
matrix[41][21]  ='X'
matrix[41][22]  ='X'
matrix[40][22]  ='X'
matrix[39][21]  ='X'

matrix[40][0]  ='O'
matrix[40][1]  ='O'
matrix[40][4]  ='O'
matrix[40][5]  ='O'
matrix[40][6]  ='O'
matrix[40][7]  ='O'
matrix[40][8]  ='O'
matrix[40][9]  ='O'
matrix[40][12] ='O'
matrix[40][13] ='O'
matrix[40][14] ='O'
matrix[40][16] ='O'
matrix[40][17] ='O'
matrix[40][18] ='O'
matrix[40][19] ='O'






def wrap(r, c, R=R, C=C):
    return (r % R, c % C)

def count_neighbors(r, c, matrix=matrix, R=R, C=C):
    xneighbors = 0
    yneighbors = 0
    sum_neighbors = 0
    for row_check in (-1, 0, 1):
        for col_check in (-1, 0, 1):
            if (row_check == 0) and (col_check == 0):
                continue
            cell_row, cell_col = wrap((r + row_check), (c + col_check), R=R, C=C)
            if matrix[cell_row][cell_col] == 'X':
                xneighbors += 1
            elif matrix[cell_row][cell_col] == 'O':
                yneighbors += 1
                #print "cell %s has neighbor: %s" % ((r, c), (cell_row, cell_col))
    return {'x': xneighbors, 'o': yneighbors, 'sum': xneighbors + yneighbors}

def generate_next_X(matrix):
    next = create_matrix(len(matrix), len(matrix[0]))
    for row in range(len(matrix)):
        for cell in range(len(matrix[0])):
            count = count_neighbors(row, cell, matrix)
            current = matrix[row][cell]
            
            if current in ['X']: # HA! substitute `not in` for `in` here
                if count['x'] < 2:
                    next[row][cell] = ' '
                elif count['x'] in [2, 3]:
                    next[row][cell] = current
                elif count['x'] < 3:
                    next[row][cell] = ' '
            elif count['x'] == 3: # empty cell and exactly 3 neighbors
                next[row][cell] = 'X'
            elif current in ['O']:
                next[row][cell] = current
    return next

def generate_next_O(matrix):
    next = create_matrix(len(matrix), len(matrix[0]))
    for row in range(len(matrix)):
        for cell in range(len(matrix[0])):
            
            count = count_neighbors(row, cell, matrix)
            current = matrix[row][cell]
            if current in ['O']: # HA! substitute `not in` for `in` here
                if count['o'] < 2:
                    next[row][cell] = ' '
                elif count['o'] in [2, 3]:
                    next[row][cell] = current
                elif count['o'] < 3:
                    next[row][cell] = ' '
            elif count['o'] == 3:
                next[row][cell] = 'O'
            elif current in ['X']:
                next[row][cell] = current
    return next

def show_matrix(matrix, count1, count2):
    for line in matrix:
        sys.stdout.write("%s\n" % str(line).replace(',', '').replace("'", "").replace("[", "").replace("]", ""))
    sys.stdout.write('slow x: %d fast o: %d\n' % (count1, count2))    
    
count1 = 0
count2 = 0
while 1:
    show_matrix(matrix, count1, count2)
    matrix = generate_next_X(matrix)
    count1 += 1
    sleep(.04)

    show_matrix(matrix, count1, count2)
    matrix = generate_next_O(matrix)
    count2 += 1 
    sleep(.04)

    show_matrix(matrix, count1, count2)
    matrix = generate_next_O(matrix)
    count2 += 1 
    sleep(.04)
