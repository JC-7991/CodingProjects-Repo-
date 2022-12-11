# Given a array of numbers representing the stock 
# prices of a company in chronological order, write 
# a function that calculates the maximum profit you 
# could have made from buying and selling that stock once. 
# You must buy before you can sell it.

def maxProfit(price, start, end):
 
    if(end <= start):
        return 0
 
    profit = 0
 
    for i in range(start, end, 1):
        for j in range(i + 1, end + 1):
 
            if(price[j] > price[i]):

                curr_profit = price[j] - price[i] + \
                    maxProfit(price, start, i - 1) + \
                    maxProfit(price, j + 1, end)
 
                profit = max(profit, curr_profit)
 
    return profit
 
if __name__ == '__main__':

    price = [5, 9, 8, 11, 10, 7]
    n = len(price)
    x = n - 1
    print(maxProfit(price, 0, x))