# You are given an array of non-negative integers that represents 
# a two-dimensional elevation map where each element is unit-width 
# wall and the integer is the height. Suppose it will rain and all 
# spots between two walls get filled up. 
# Compute how many units of water remain trapped on the map 
# in O(N) time and O(1) space.

def max_water(arr, x):
  
    res = 0
  
    for i in range(1, x - 1):
 
        left = arr[i]

        for j in range(i):
            left = max(left, arr[j])

        right = arr[i]
  
        for j in range(i + 1, x):
            right = max(right, arr[j])

        res = res + (min(left, right) - arr[i])
  
    return res
  
if __name__ == "__main__":
  
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    x = len(arr)
    print(max_water(arr, x))

    arr2 = [1, 0, 3, 1, 2, 2, 1, 0, 0, 1, 0, 1]
    x2 = len(arr2)
    print(max_water(arr2, x2))

    arr3 = [7, 8, 12, 0, 2, 1, 32, 12, 10, 11, 0, 14, 0, 0, 34]
    x3 = len(arr3)
    print(max_water(arr3, x3))

    arr4 = [1, 2, 3, 0, 3, 2, 1]
    x4 = len(arr4)
    print(max_water(arr4, x4))