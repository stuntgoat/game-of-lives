#!/usr/local/bin/python3.3

# Any live cell with fewer than two live neighbours dies, as if caused by under-population.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overcrowding.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


def create_2x2_matrix(r, c):
    return [[0 for i in range(r)] for j in range(c)]

matrix = create_2x2_matrix(10, 10)

matrix[4][3] = 1

def wrap(r, c, matrix):
    row = None
    col = None
    if (r > (len(matrix) - 1)) or (r < 0):
        row = r % len(matrix)
    else:
        row = r
    if (c > (len(matrix) - 1)) or (c < 0):
        col = c % len(matrix[0])
    else:
        col = c
    return (row, col)

def check_neighbors(r, c, matrix):
    neighbors = []
    rows = len(matrix)
    cols = len(matrix[0])
    for row_i in range(rows): # each row in matrix
        for col_i in range(cols) : # each column
            for row_check in (-1, 0, 1):
                for col_check in (-1, 0, 1):
                    if (row_check == 0) and (col_check == 0):
                        pass
                    else:
                        cell_row, cell_col = wrap((r + row_check), (c + col_check),  matrix)
                        if matrix[cell_row][cell_col] == 1:
                            neighbors.append([cell_row, cell_col])
            if len(neighbors) > 0:
                print("cell has neighbor")
 
for row in range(len(matrix)):
    for cell in range(len(matrix[0])):
        check_neighbors(row, cell, matrix)

                    
        
