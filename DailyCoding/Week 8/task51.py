# Given a function that generates perfectly random
# numbers between 1 and k (inclusive), where k is an
# input, write a function that shuffles a deck of cards 
# represented as an array using only swaps.
# It should run in O(N) time.

from random import randint

def randomizer (arr, k):

    for i in range(k - 1, 0, -1):
        j = randint(0, i + 1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr

if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    k = len(arr)
    print(randomizer(arr, k))