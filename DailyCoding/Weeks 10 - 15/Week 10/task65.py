# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

def spiral(matrix):

    ans = []
    m = len(matrix)
    n = len(matrix[0])

    seen = [[0 for i in range(n)] for j in range(m)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    x = 0
    y = 0
    z = 0
 
    for i in range(m * n):

        ans.append(matrix[x][y])
        seen[x][y] = True
        cr = x + dr[z]
        cc = y + dc[z]
 
        if (0 <= cr and cr < m and 0 <= cc and cc < n and not(seen[cr][cc])):
            x = cr
            y = cc

        else:
            z = (z + 1) % 4
            x += dr[z]
            y += dc[z]

    return ans

if __name__ == "__main__":

    a = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]
 
    for x in spiral(a):
        print(x, end = " ")