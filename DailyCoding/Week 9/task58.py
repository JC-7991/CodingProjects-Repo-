# An sorted array of integers was rotated an unknown number of times.
# Given such an array, find the index of the element in the array 
# in faster than linear time. If the element doesn't exist in the array, return null.

def pivotSearch(arr, n, key):
 
    pivot = pivotFind(arr, 0, n-1)
 
    if pivot == -1:
        return binarySearch(arr, 0, n-1, key)
 
    if arr[pivot] == key:
        return pivot

    if arr[0] <= key:
        return binarySearch(arr, 0, pivot - 1, key)

    return binarySearch(arr, pivot + 1, n - 1, key)

def pivotFind(arr, low, high):
 
    if high < low:
        return -1

    if high == low:
        return low

    mid = int((low + high)/2)
 
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid

    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid - 1)

    if arr[low] >= arr[mid]:
        return pivotFind(arr, low, mid - 1)

    return pivotFind(arr, mid + 1, high)

def binarySearch(arr, low, high, key):
 
    if high < low:
        return -1

    mid = int((low + high) / 2)
 
    if key == arr[mid]:
        return mid

    if key > arr[mid]:
        return binarySearch(arr, (mid + 1), high, key)

    return binarySearch(arr, low, (mid - 1), key)
 
if __name__ == "__main__":

    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    arr = [3, 7, 10, 3, 4, 2, 1, 1, 9]
    print("Index of the element is:", \
        pivotSearch(arr, len(arr), 10))