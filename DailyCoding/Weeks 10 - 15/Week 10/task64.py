# A knight's tour is a sequence of moves by a knight 
# on a chessboard such that all squares are visited once.
# Given N, write a function to return the number of 
# knight's tours on an N by N chessboard.

n = 8

def safe(x, y, board):

    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True

    return False
 
def printAll(n, board):

    for i in range(n):
        for j in range(n):
            print(board[i][j], end = ' ')
            
        print()
 
def solveKnight(n):

    board = [[-1 for i in range(n)] for i in range(n)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0] = 0
    pos = 1

    if(not solveTour(n, board, 0, 0, move_x, move_y, pos)):
        print("Solution not found.")
    else:
        printAll(n, board)
 
 
def solveTour(n, board, curr_x, curr_y, move_x, move_y, pos):

    if(pos == n ** 2):
        return True
 
    for i in range(8):

        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]

        if(safe(new_x, new_y, board)):

            board[new_x][new_y] = pos

            if(solveTour(n, board, new_x, new_y, move_x, move_y, pos + 1)):
                return True

            board[new_x][new_y] = -1

    return False
 
if __name__ == "__main__":
    solveKnight(n)