# Given a 2D matrix of characters and a target word, 
# write a function that returns whether the word 
# can be found in the matrix by going left-to-right, or up-to-down.
# For example, given the following matrix:
# [['F', 'A', 'C', 'I'],
# ['O', 'B', 'Q', 'P'],
# ['A', 'N', 'O', 'B'],
# ['M', 'A', 'S', 'S']]
#and the target word 'FOAM', you should return true, 
# since it's the leftmost column. Similarly, given the 
# target word 'MASS', you should return true, since it's the last row.

from typing import List

def wordOccurance(matrix: List[List[str]], word: str) -> bool:

    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):

        row = "".join(matrix[i])

        if word in row:
            return True

    for j in range(m):

        column = ""

        for i in range(n):
            column += matrix[i][j]

        if word in column:
            return True

    return False


if __name__ == "__main__":

    matrix = [
        ["F", "A", "C", "I"],
        ["O", "B", "Q", "P"],
        ["A", "N", "O", "B"],
        ["M", "A", "S", "S"],
    ]

    print(wordOccurance(matrix, "FOAM"))
    print(wordOccurance(matrix, "MASS"))
    print(wordOccurance(matrix, "FORM"))