# A number is considered perfect if its digits sum up to exactly 10.
# Given a positive integer n, return the n-th perfect number.
# For example, given 1, you should return 19. Given 2, you should return 28.

import itertools

def findNth(n):
 
    count = 0
 
    for cnt in itertools.count():

        sum = 0
        x = cnt

        while(x):
            sum = sum + x % 10
            x = x // 10

        if(sum == 10):
            count = count + 1

        if (count == n):
            return cnt
 
    return -1

if __name__== "__main__":

    print(findNth(1))
    print(findNth(2))