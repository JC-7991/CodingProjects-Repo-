# Given an array of strictly the characters 'R', 'G', and 'B', 
# segregate the values of the array so that all the Rs come first,
# the Gs come second, and the Bs come last. You can only swap elements of the array.

def sorted(chars):

    left, right = 0, len(chars) - 1

    while True:

        while chars[left] == 'R' and left < right:
            left += 1

        while chars[right] != 'R' and left < right:
            right -= 1

        if left >= right:
            break

        chars[left], chars[right] = chars[right], chars[left]

    right = len(chars) - 1

    while True:

        while chars[left] != 'B' and left < right:
            left += 1

        while chars[right] == 'B' and left < right:
            right -= 1

        if left >= right:
            break

        chars[left], chars[right] = chars[right], chars[left]

    return chars

if __name__ == '__main__':
    print (sorted(['G', 'B', 'R', 'R', 'B', 'R', 'G']))