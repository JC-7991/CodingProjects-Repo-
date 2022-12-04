# Implement Conway's Game of Life. It should be able to be initialized 
# with a starting list of live cell coordinates and the number of 
# steps it should run for. Once initialized, it should print out 
# the board state at each step. Since it's an infinite board, print 
# out only the relevant coordinates, i.e. from the top-leftmost 
# live cell to bottom-rightmost live cell.

def nextGeneration(grid, M, N):

    future = [[0 for i in range(N)] for j in range(M)]

    for l in range(M):
        for m in range(N):
             
            aliveNeighbours = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    if ((l+i>=0 and l+i<M) and (m+j>=0 and m+j<N)):
                        aliveNeighbours += grid[l + i][m + j]
 
            aliveNeighbours -= grid[l][m]
 
            if ((grid[l][m] == 1) and (aliveNeighbours < 2)):
                future[l][m] = 0

            elif ((grid[l][m] == 1) and (aliveNeighbours > 3)):
                future[l][m] = 0

            elif ((grid[l][m] == 0) and (aliveNeighbours == 3)):
                future[l][m] = 1
 
            else:
                future[l][m] = grid[l][m]
 
 
    print("Next Generation")
    for i in range(M):
        for j in range(N):
            if (future[i][j] == 0):
                print(".",end="")
            else:
                print("*",end="")
        print()
 
M, N = 10,10
grid = [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ],
    [ 0, 0, 1, 1, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
]

print("Original Generation")
for i in range(M):
    for j in range(N):
        
        if(grid[i][j] == 0):
            print(".",end = "")
        else:
            print("*",end = "")
    print()
print()
nextGeneration(grid, M, N)