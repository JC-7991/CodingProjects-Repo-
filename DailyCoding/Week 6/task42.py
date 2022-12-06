# Given a list of integers S and a target number k,
# write a function that returns a subset of S that 
# adds up to k. If such a subset cannot be made, then return null.

def is_subset(set, x, sum):

    if(sum == 0):
        return True

    if(x == 0):
        return False
  
    if(set[x - 1] > sum):
        return is_subset(set, x - 1, sum)
  
    return is_subset(set, x - 1, sum) or is_subset(set, x - 1, sum - set[x - 1])
  
if __name__  == "__main__":

    set = [3, 34, 7, 10, 15]
    sum = 9
    x = len(set)

    if(is_subset(set, x, sum) == True):
        print("Found a subset with given sum.")

    else:
        print("No subset with given sum.")

    set = [5, 10, 15, 20, 25]
    sum = 30
    x = len(set)

    if(is_subset(set, x, sum) == True):
        print("Found a subset with given sum.")

    else:
        print("No subset with given sum.")