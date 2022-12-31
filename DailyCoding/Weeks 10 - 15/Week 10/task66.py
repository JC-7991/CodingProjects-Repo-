# Assume you have access to a function toss_biased() 
# which returns 0 or 1 with a probability that's not 
# 50-50 (but also not 0-100 or 100-0). You do not know 
# the bias of the coin.
# Write a function to simulate an unbiased coin toss.

import random

def unbiasedCoin():
    return random.choice(['H','T'])

def biasedCoin():
    return random.choice(['H','T', 'H'])

if __name__ == "__main__":

    print('COIN FLIP: ', unbiasedCoin())
    print('COIN FLIP: ', biasedCoin())
    print('COIN FLIP: ', unbiasedCoin())
    print('COIN FLIP: ', biasedCoin())
    print('COIN FLIP: ', unbiasedCoin())
    print('COIN FLIP: ', biasedCoin())