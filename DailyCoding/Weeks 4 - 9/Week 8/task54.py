# Sudoku is a puzzle where you're given a 
# partially-filled 9 by 9 grid with digits. 
# The objective is to fill the grid with the 
# constraint that every row, column, and box 
# (3 by 3 subgrid) must contain all of the digits from 1 to 9.
# Implement an efficient sudoku solver.

N = 9

def printGrid(arr):

    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()
 
def isSafe(grid, row, col, num):
   
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False
 
    startRow = row - row % 3
    startCol = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
def solve(grid, row, col):
   
    if(row == N - 1 and col == N):
        return True
       
    if col == N:
        row += 1
        col = 0
 
    if grid[row][col] > 0:
        return solve(grid, row, col + 1)

    for num in range(1, N + 1, 1):
       
        if isSafe(grid, row, col, num):
           
            grid[row][col] = num
 
            if solve(grid, row, col + 1):
                return True

        grid[row][col] = 0

    return False
 
if __name__ == "__main__":

    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    
    if(solve(grid, 0, 0)):
        printGrid(grid)

    else:
        print("No solution exists.")