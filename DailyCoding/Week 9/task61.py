# Implement integer exponentiation. That is, implement 
# the pow(x, y) function, where x and y are integers and returns x^y.
# Do this faster than the naive method of repeated multiplication.
# For example, pow(2, 10) should return 1024.

def power(base, power):

    if power == 0:
        return 1

    if power % 2 != 0:
        return pow((base * base), power // 2) * base

    return pow((base * base), power // 2)


if __name__ == "__main__":

    print(power(1, 10))
    print(power(2, 10))
    print(power(3, 10))
