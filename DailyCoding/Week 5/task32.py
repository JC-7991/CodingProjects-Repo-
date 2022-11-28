# Suppose you are given a  of currency exchange rates, represented as a 2D array. 
# Determine whether there is a possible arbitrage: that is, whether 
# there is some  sequence of trades you can make, 
# starting with some amount A of any currency, so 
# that you can end up with some amount greater than A of that currency.

from typing import Tuple, List
from math import log

rates = [
    [1, 0.23, 0.25, 16.43, 18.21, 4.94],
    [4.34, 1, 1.11, 71.40, 79.09, 21.44],
    [3.93, 0.90, 1, 64.52, 71.48, 19.37],
    [0.061, 0.014, 0.015, 1, 1.11, 0.30],
    [0.055, 0.013, 0.014, 0.90, 1, 0.27],
    [0.20, 0.047, 0.052, 3.33, 3.69, 1],
]

currencies = ('PLN', 'EUR', 'USD', 'RUB', 'INR', 'MXN')

def negate_logarithm_convertor(graph: Tuple[Tuple[float]]) -> List[List[float]]:
    result = [[-log(edge) for edge in row] for row in graph]
    return result

def arbitrage(currency_tuple: tuple, rates_matrix: Tuple[Tuple[float, ...]]):

    trans_graph = negate_logarithm_convertor(rates_matrix)
    source = 0

    n = len(trans_graph)
    min_dist = [float('inf')] * n
    
    pre = [-1] * n
    min_dist[source] = source

    for _ in range(n - 1):
        for source_curr in range(n):
            for dest_curr in range(n):

                if min_dist[dest_curr] > min_dist[source_curr] + trans_graph[source_curr][dest_curr]:
                    min_dist[dest_curr] = min_dist[source_curr] + trans_graph[source_curr][dest_curr]
                    pre[dest_curr] = source_curr

    for source_curr in range(n):
        for dest_curr in range(n):

            if min_dist[dest_curr] > min_dist[source_curr] + trans_graph[source_curr][dest_curr]:

                print_cycle = [dest_curr, source_curr]
    
                while pre[source_curr] not in  print_cycle:
                    print_cycle.append(pre[source_curr])
                    source_curr = pre[source_curr]

                print_cycle.append(pre[source_curr])
                print("Arbitrage Opportunity: \n")
                print(" --> ".join([currencies[p] for p in print_cycle[::-1]]))


if __name__ == "__main__":
    arbitrage(currencies, rates)