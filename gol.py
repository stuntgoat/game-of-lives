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
matrix[11][2]  ='O'
matrix[12][0]  ='O'
matrix[12][2]  ='O'
matrix[13][1]  ='O'
matrix[13][2]  ='O'
matrix[7][5]   ='O'
matrix[8][5]   ='O'
matrix[8][7]   ='O'
matrix[9][5]   ='O'
matrix[9][6]   ='O'
matrix[33][2]  ='X'
matrix[33][3]  ='X'
matrix[33][4]  ='X'
matrix[32][4]  ='X'
matrix[33][3]  ='X'
matrix[15][14] ='O'
matrix[14][14] ='O'
matrix[13][14] ='O'
matrix[12][14] ='O'
matrix[11][14] ='O'
matrix[10][14] ='O'
matrix[24][2]  ='X'
matrix[24][3]  ='X'
matrix[24][4]  ='X'
matrix[23][4]  ='X'
matrix[22][3]  ='X'
matrix[24][2]  ='X'
matrix[24][3]  ='X'
matrix[24][4]  ='X'
matrix[23][4]  ='X'
matrix[22][3]  ='X'
matrix[41][2]  ='X'
matrix[41][3]  ='X'
matrix[41][4]  ='X'
matrix[40][4]  ='X'
matrix[39][3]  ='X'
matrix[41][20]  ='O'
matrix[41][21]  ='O'
matrix[41][22]  ='O'
matrix[40][22]  ='O'
matrix[39][21]  ='O'

matrix[40][0]  ='X'
matrix[40][1]  ='X'
matrix[40][4]  ='X'
matrix[40][5]  ='X'
matrix[40][6]  ='X'
matrix[40][7]  ='X'
matrix[40][8]  ='X'
matrix[40][9]  ='X'
matrix[40][12]  ='X'
matrix[40][13]  ='X'
matrix[40][14]  ='X'
matrix[40][16]  ='X'
matrix[40][17]  ='X'
matrix[40][18]  ='X'
matrix[40][19]  ='X'







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
                if count['sum'] < 2:
                    next[row][cell] = ' '
                elif count['sum'] in [2, 3]:
                    next[row][cell] = current
                elif count['sum'] < 3:
                    next[row][cell] = ' '
            elif current in ['O']: # current is occupied
                next[row][cell] = current
            elif count['sum'] == 3: # empty cell and exactly 3 neighbors
                if count['x'] > count['o']:
                    next[row][cell] = 'X'
                else:
                    next[row][cell] = 'O'
    return next

def generate_next_O(matrix):
    next = create_matrix(len(matrix), len(matrix[0]))
    for row in range(len(matrix)):
        for cell in range(len(matrix[0])):
            count = count_neighbors(row, cell, matrix)
            last = matrix[row][cell]
            if last in ['O']: # HA! substitute `not in` for `in` here
                if count['sum'] < 2:
                    next[row][cell] = ' '
                elif count['sum'] in [2, 3]:
                    next[row][cell] = last
                elif count['sum'] < 3:
                    next[row][cell] = ' '
            elif last in ['X']:
                next[row][cell] = last
            elif count['sum'] == 3:
                if count['x'] > count['o']:
                    next[row][cell] = 'X'
                else:
                    next[row][cell] = 'O'
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
    sleep(.06)

    show_matrix(matrix, count1, count2)
    matrix = generate_next_O(matrix)
    count2 += 1 
    sleep(.06)

    show_matrix(matrix, count1, count2)
    matrix = generate_next_O(matrix)
    count2 += 1 
    sleep(.06)

        
