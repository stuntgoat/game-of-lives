#!/usr/local/bin/python3.3
from time import sleep
import sys

from seed_matrix import R, C, MATRIX, create_matrix

def wrap(r, c, R=R, C=C):
    return (r % R, c % C)

def count_neighbors(r, c, matrix=MATRIX, R=R, C=C):
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
            
            if current in ['X']: 
                if count['x'] < 2:
                    next[row][cell] = ' '
                elif count['x'] in [2, 3]:
                    next[row][cell] = current
                elif count['x'] < 3:
                    next[row][cell] = ' '
            elif count['x'] == 3:
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
            if current in ['O']: 
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
matrix = MATRIX
while 1:
    show_matrix(matrix, count1, count2)
    matrix = generate_next_X(matrix)
    count1 += 1
    sleep(.5)

    show_matrix(matrix, count1, count2)
    matrix = generate_next_O(matrix)
    count2 += 1 
    sleep(.5)

    show_matrix(matrix, count1, count2)
    matrix = generate_next_O(matrix)
    count2 += 1 
    sleep(.5)
