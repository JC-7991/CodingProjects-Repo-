# The power set of a set is the set of all its subsets. 
# Write a function that, given a set, generates its power set.

import math;
 
def powerSet(set, size):
     
    pow_size = (int) (math.pow(2, size))
    counter = 0
    j = 0

    for counter in range(0, pow_size):
        for j in range(0, size):
            if((counter & (1 << j)) > 0):
                print(set[j], end = "")
        print("")

if __name__ == "__main__":
    set = ['a', 'b', 'c']
    powerSet(set, 3)