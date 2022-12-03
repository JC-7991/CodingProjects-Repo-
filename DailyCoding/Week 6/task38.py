# You have an N by N board. Write a function that, given N,
# returns the number of possible arrangements of the board 
# where N queens can be placed on the board without 
# threatening each other, i.e. no two queens share the
# same row, column, or diagonal.

def is_safe(space, x, y):
 
    for i in range(x):
        if space[i][y] == 'Q':
            return False
 
    (i, j) = (x, y)

    while i >= 0 and j >= 0:
        if space[i][j] == 'Q':
            return False

        i = i - 1
        j = j - 1
 
    (i, j) = (x, y)

    while i >= 0 and j < len(space):
        if space[i][j] == 'Q':
            return False

        i = i - 1
        j = j + 1
 
    return True
 
def printSolution(space):

    for x in space:
        print(str(x).replace(',', '').replace('\'', ''))
    print()
 
def nQueen(space, x):
 
    if x == len(space):
        printSolution(space)
        return
 
    for i in range(len(space)):

        if is_safe(space, x, i):

            space[x][i] = 'Q'
            nQueen(space, x + 1)
            space[x][i] = '–'
 
 
if __name__ == '__main__':

    N = 8
    space = [['–' for x in range(N)] for y in range(N)]
    nQueen(space, 0)