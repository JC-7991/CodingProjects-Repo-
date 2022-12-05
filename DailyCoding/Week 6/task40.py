# Given an array of integers where every integer
# occurs three times except for one integer, which 
# only occurs once, find and return the non-duplicated integer.

def singleElement(arr, x):

    ones = 0
    twos = 0
     
    for i in range(x):

        twos = twos ^ (ones & arr[i])
        ones = ones ^ arr[i]
        common_bit_mask = ~(ones & twos)
        ones &= common_bit_mask
        twos &= common_bit_mask

    return ones

if __name__ == "__main__":

    arr = [3, 3, 3, 2]
    x = len(arr)
    print("The element with single occurrence is", singleElement(arr, x))