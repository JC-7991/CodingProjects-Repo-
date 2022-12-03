# You have an N by N board. Write a function that, given N,
# returns the number of possible arrangements of the board 
# where N queens can be placed on the board without 
# threatening each other, i.e. no two queens share the
# same row, column, or diagonal.

def is_safe(mat, x, y):
 
    for i in range(x):
        if mat[i][y] == 'Q':
            return False
 
    (i, j) = (x, y)

    while i >= 0 and j >= 0:
        if mat[i][j] == 'Q':
            return False

        i = i - 1
        j = j - 1
 
    (i, j) = (x, y)

    while i >= 0 and j < len(mat):
        if mat[i][j] == 'Q':
            return False

        i = i - 1
        j = j + 1
 
    return True
 
def printSolution(mat):

    for x in mat:
        print(str(x).replace(',', '').replace('\'', ''))
    print()
 
def nQueen(mat, x):
 
    if x == len(mat):
        printSolution(mat)
        return
 
    for i in range(len(mat)):

        if is_safe(mat, x, i):

            mat[x][i] = 'Q'

            nQueen(mat, x + 1)
 
            mat[x][i] = '–'
 
 
if __name__ == '__main__':

    N = 8

    mat = [['–' for x in range(N)] for y in range(N)]
 
    nQueen(mat, 0)