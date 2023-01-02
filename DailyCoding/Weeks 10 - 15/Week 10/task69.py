# Given a list of integers, return the largest product that can be made by multiplying any three integers.
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
# You can assume the list has at least three integers.

import sys

def largest(arr, n):
 
    if n < 3:
        return -1

    maxProd = -(sys.maxsize - 1)
     
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):

                maxProd = max(maxProd, arr[i] * arr[j] * arr[k])
 
    return maxProd
 
if __name__ == "__main__":

    arr = [-10, -10, 5, 2]
    n = len(arr)
    
    max = largest(arr, n)
    
    if max == -1:
        print("No max product found.")

    else:
        print("Maximum product is", max)