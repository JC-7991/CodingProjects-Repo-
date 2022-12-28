# Given an undirected graph represented as an 
# adjacency matrix and an integer k, write a 
# function to determine whether each vertex in 
# the graph can be colored such that no two adjacent 
# vertices share the same color using at most k colors.

from typing import List

def colorable(matrix: List[List[int]], k: int) -> bool:

    min_color = 0
    vert = len(matrix)

    for vertex in range(vert):

        current_colors = sum(matrix[vertex]) + 1
        min_color = max(min_color, current_colors)

    return min_color <= k


if __name__ == "__main__":

    matrix = [
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 0],
    ]

    print(colorable(matrix, 5))
    print(colorable(matrix, 4))
    print(colorable(matrix, 3))
    print(colorable(matrix, 2))
    print(colorable(matrix, 1))