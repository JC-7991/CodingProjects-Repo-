# There is an N by M matrix of zeroes. Given N and M,
# write a function to count the number of ways of starting 
# at the top-left corner and getting to the bottom-right corner. 
# You can only move right or down.
# For example, given a 2 by 2 matrix, you should return 2, 
# since there are two ways to get to the bottom-right:
# Right, then down
# Down, then right
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

def paths(m, n):

    if(m == 1 or n == 1):
        return 1

    return paths(m - 1, n) + paths(m, n - 1)
 
if __name__ == "__main__":
    
    m = 3
    n = 3
    print(paths(m, n))