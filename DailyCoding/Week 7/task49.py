# Given an array of numbers, find the maximum sum of any 
# contiguous subarray of the array.
# For example, given the array [34, -50, 42, 14, -5, 86],
# the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
# Given the array [-5, -1, -8, -9], the maximum sum would be 0, 
# since we would not take any elements.
# Do this in O(N) time.

from xmlrpc.client import MAXINT

def maxSub(a, size):
 
    maxFar = -MAXINT - 1
    maxEnding = 0
 
    for i in range(0, size):

        maxEnding = maxEnding + a[i]

        if(maxFar < maxEnding):
            maxFar = maxEnding
 
        if maxEnding < 0:
            maxEnding = 0

    return maxFar

if __name__ == "__main__":

    a = [34, -50, 42, 14, -5, 86]
    print("Maximum contiguous sum is", maxSub(a, len(a)))

    b = [-5, -1, -8, -9]
    print("Maximum contiguous sum is", maxSub(b, len(b)))