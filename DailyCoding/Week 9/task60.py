# Given a multiset of integers, return whether it 
# can be partitioned into two subsets whose sums are the same.
# For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, 
# it would return true, since we can split it up into 
# {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.
# Given the multiset {15, 5, 20, 10, 35}, it would return false, 
# since we can't split it up into two subsets that add up to the same sum.

def isSubsetSum(arr, n, sum):

    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    if arr[n - 1] > sum:
        return isSubsetSum(arr, n - 1, sum)
 
    return isSubsetSum(arr, n - 1, sum) or isSubsetSum(arr, n - 1, sum - arr[n - 1])
 
def findPartion(arr, n):

    sum = 0

    for i in range(0, n):
        sum += arr[i]

    if sum % 2 != 0:
        return False

    return isSubsetSum(arr, n, sum // 2)

if __name__ == "__main__":

    arr = [4, 12, 3, 8, 7, 48]
    n = len(arr)
 
    if findPartion(arr, n) == True:
        print("Can be divided into two subsets of equal sum.")
    else:
        print("Can not be divided into two subsets of equal sum.")
 