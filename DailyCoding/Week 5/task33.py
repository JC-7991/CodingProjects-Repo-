# Compute the running median of a sequence of numbers. 
# That is, given a stream of numbers, print out the median 
# of the list so far on each new element.
# Recall that the median of an even-numbered list is 
# the average of the two middle numbers.

def binarySearch(arr, item, low, high):
 
    if (low >= high):
        return (low + 1) if (item > arr[low]) else low
 
    mid = (low + high) // 2
 
    if (item == arr[mid]):
        return mid + 1
 
    if (item > arr[mid]):
        return binarySearch(arr, item, mid + 1, high)
 
    return binarySearch(arr, item, low, mid - 1)
 
def printMedian(arr, n):
 
    i, j, pos, num = 0, 0, 0, 0
    count = 1
 
    print(f"Median after reading 1 element is {arr[0]}")
 
    for i in range(1, n):

        median = 0
        j = i - 1
        num = arr[i]
        pos = binarySearch(arr, num, 0, j)

        while (j >= pos):
            arr[j + 1] = arr[j]
            j -= 1
 
        arr[j + 1] = num
 
        count += 1
 
        if (count % 2 != 0):
            median = arr[count // 2]
 
        else:
            median = (arr[(count // 2) - 1] + arr[count // 2]) // 2
 
        print(f"Median after reading {i + 1} elements is {median} ")

if __name__ == "__main__":
 
    arr = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
    n = len(arr)
    printMedian(arr, n)