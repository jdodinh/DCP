"""
Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a
possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of
any currency, so that you can end up with some amount greater than A of that currency.
"""

import pandas as pd
from itertools import permutations


# Each node will be representative of a currency, and will contain a dictionary of (currency, exchange rate) k, v pairs
class GraphNode:
    def __init__(self, name):
        self.currency = name
        self.neighbors = {}


# array representing the exchange rates
curr_array = [
    [1, 0.9045, 0.8249,	108.17,	0.9943,	1.3213,	1.4598],
    [1.1056,	1,	0.9119,	119.59,	1.0992,	1.4607,	1.6139],
    [1.2123, 1.0967, 1,	131.14, 1.2054,	1.6017,	1.7699],
    [0.00924, 0.00836, 0.00763, 1, 0.009192, 0.01221, 0.01350],
    [1.0058, 0.9098, 0.8297, 108.80, 1, 1.3285, 1.4681],
    [0.7570, 0.6847, 0.6245, 81.89, 0.7526, 1, 1.1050],
    [0.6850, 0.6196, 0.5651, 74.10, 0.6811, 0.9050, 1]
]


# list of currencies, ordered such that it matches the curr_array
curr = [
    'USD',
    'EUR',
    'GBP',
    'JPY',
    'CHF',
    'CAD',
    'AUD'
]

# initialized dictionary of nodes
nodes = {}


# Given a list of exchange rates, this function evaluates the final amount of USD, once the exchanges have been made in
# the order specified by the list
def cycle_val(currencies: list):
    # end = cycle_val(sample)
    nd = iter(currencies)                       # creating an iterator
    val = 1                                     # start with 1 USD
    for cur in currencies[1:]:                  # Loop throgh currencies in order specified by list
        node = nodes[next(nd)]                  # Fetch the node specified by currency currently held (initially USD)
        val = node.neighbors[cur] * val         # exchange is calculated
    val = nodes[next(nd)].neighbors[currencies[0]] * val    # Finally the exchange rate back to USD is evaluated
    return val


def main():
    debug = False
    extr = []                                   # Initialize empty list of Cycle, Value pairs
    for i in range(len(curr)):                  # Initializing the graph nodes based on currencies given
        node = GraphNode(curr[i])               # Setting name of node
        nodes[curr[i]] = node                   # Adding to dictionary of nodes
        for j in range(len(curr_array[i])):     # Adding exchange rates of neighboring nodes
            if j != i:
                node.neighbors[curr[j]] = curr_array[i][j]
    for i in range(2, len(curr)):
        arr = permutations(curr[1:], i)         # Getting all permutations of currencies starting at given value
        for el in arr:                          # Calculating end value for a given permutation of exchanges
            new_curr = list(el)
            new_curr = ["USD"] + new_curr
            extr.append([el, cycle_val(new_curr)])  # Calling the function that determines value

    df = pd.DataFrame(extr, columns=["cycle", "val"])   # Creating dataframe
    df = df.sort_values(by="val", ascending=False)
    df.to_csv("./currency_csv.csv")
    print(df.values)                            # Printing values


if __name__=="__main__":
    main()