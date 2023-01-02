# On our special chessboard, two bishops attack each 
# other if they share the same diagonal. This includes 
# bishops that have another bishop located between them, 
# i.e. bishops can attack through pieces.
# You are given N bishops, represented as (row, column) 
# tuples on a M by M chessboard. Write a function to count 
# the number of pairs of bishops that attack each other. The 
# ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).
# For example, given M = 5 and the list of bishops:
# (0, 0)
# (1, 2)
# (2, 2)
# (4, 0)
# The board would look like this:
# [b 0 0 0 0]
# [0 0 b 0 0]
# [0 0 b 0 0]
# [0 0 0 0 0]
# [b 0 0 0 0]
# You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.

def printBoard(M, bishops):

    board = [['.' for i in range(M)] for j in range(M)]

    for bishop in bishops:
        y, x = bishop[0], bishop[1]
        board[y][x] = 'b'

    for row in board:
        for e in row:
            print(e, end = '\t')
        print("\n")


def bishopAttack(x, bishops):

    nonPair = 0

    for i in range(len(bishops) - 1):

        y1, x1 = bishops[i][0], bishops[i][1]

        for j in range(i + 1, len(bishops)):

            y2, x2 = bishops[j][0], bishops[j][1]

            if abs(x1 - x2) == abs(y1 - y2):
                nonPair += 1

    return nonPair


def attackTest(M, bishops):
    
    printBoard(M, bishops)
    print('No. pairs of attacking bishops:', bishopAttack(M, bishops))

if __name__ == "__main__":
    
    attackTest(M = 5, bishops = [(0, 0), (1, 2), (2, 2), (4, 0)])
    attackTest(M = 5, bishops = [(0, 4), (1, 2), (2, 2), (4, 0)])