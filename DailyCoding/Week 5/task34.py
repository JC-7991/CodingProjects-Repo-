# Given a string, find the palindrome that
# can be made by inserting the fewest number 
# of characters as possible anywhere in the word. 
# If there is more than one palindrome of 
# minimum length that can be made, return 
# the lexicographically earliest one (the first one alphabetically).

import sys
 
def min_insert(str, x, y):

    if(x > y):
        return sys.maxsize

    if(x == y):
        return 0

    if(x == y - 1):
        return 0 if(str[x] == str[y]) else 1
     
    if(str[x] == str[y]):
        return min_insert(str, x + 1, y - 1)

    else:
        return(min(min_insert(str, x, y - 1), min_insert(str, x + 1, y)) + 1)

if __name__ == "__main__":
     
    str = "sonicheroes"
    print(min_insert(str, 0, len(str) - 1))

    str = "racecar"
    print(min_insert(str, 0, len(str) - 1))
    
    str = "racecar"
    print(min_insert(str, 0, len(str) - 1))