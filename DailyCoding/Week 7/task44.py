# We can determine how "out of order" an array A is
# by counting the number of inversions it has. 
# Two elements A[i] and A[j] form an inversion if A[i] > A[j] 
# but i < j. That is, a smaller element appears after a larger element.
# Given an array, count the number of inversions it has. 
# Do this faster than O(N^2) time.

def inv_count(arr, n):
    return get_InvCount(arr)[1]

def get_InvCount(arr):

    if len(arr) <= 1:
        return arr, 0

    middle = int(len(arr) / 2)
    left, a = get_InvCount(arr[:middle])
    right, b = get_InvCount(arr[middle:])
    result, c = merge_count(left, right)

    return result, (a + b + c)

def merge_count(left, right):

    result = []
    count = 0
    i, j = 0,0
    left_len = len(left)

    while i < left_len and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            count += left_len - i
            j += 1

    result += left[i:]
    result += right[j:]
    return result, count   

if __name__ == "__main__":

    arr = [1, 2, 30, 2, 1] 
    n = len(arr) 
    print("Number of inversions:", inv_count(arr, n)) 