# Given an array of integers where every integer
# occurs three times except for one integer, which 
# only occurs once, find and return the non-duplicated integer.

def getSingle(arr, x):

    ones = 0
    twos = 0
     
    for i in range(x):

        twos = twos ^ (ones & arr[i])

        ones = ones ^ arr[i]

        mask = ~(ones & twos)

        ones &= mask

        twos &= mask

    return ones

if __name__ == "__main__":

    arr = [3, 3, 2, 3, 3]
    x = len(arr)
    print("The element with single occurrence is", getSingle(arr, x))