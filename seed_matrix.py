# used in gol.py for creating and seeding the initial matrix
R = 45
C = 45

def create_matrix(r, c):
    return [[' ' for i in range(r)] for j in range(c)]
matrix = create_matrix(R, C)
MATRIX = matrix

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
