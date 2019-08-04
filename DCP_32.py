import pandas as pd
from itertools import permutations


class GraphNode:
    def __init__(self, name):
        self.currency = name
        self.neighbors = {}


curr_array = [
    [1, 0.9045, 0.8249,	108.17,	0.9943,	1.3213,	1.4598],
    [1.1056,	1,	0.9119,	119.59,	1.0992,	1.4607,	1.6139],
    [1.2123, 1.0967, 1,	131.14, 1.2054,	1.6017,	1.7699],
    [0.00924, 0.00836, 0.00763, 1, 0.009192, 0.01221, 0.01350],
    [1.0058, 0.9098, 0.8297, 108.80, 1, 1.3285, 1.4681],
    [0.7570, 0.6847, 0.6245, 81.89, 0.7526, 1, 1.1050],
    [0.6850, 0.6196, 0.5651, 74.10, 0.6811, 0.9050, 1]
]

curr = [
    'USD',
    'EUR',
    'GBP',
    'JPY',
    'CHF',
    'CAD',
    'AUD'
]

nodes = {}


def cycle_val(currencies: list):
    # end = cycle_val(sample)
    nd = iter(currencies)
    # currencies.append(nodes[nd].currency)
    val = 1
    for cur in currencies[1:]:
        node = nodes[next(nd)]
        val = node.neighbors[cur] * val
    val = nodes[next(nd)].neighbors[currencies[0]] * val
    return val


def main():
    debug = False
    extr = []
    for i in range(len(curr)):
        node = GraphNode(curr[i])
        nodes[curr[i]] = node
        for j in range(len(curr_array[i])):
            if j != i:
                node.neighbors[curr[j]] = curr_array[i][j]
    # find_profit(nodes)
    # sample = ['USD', 'EUR', 'CHF']
    if debug is False:
        for i in range(2, len(curr)):
            arr = permutations(curr[1:], i)
            for el in arr:
                new_curr = list(el)
                new_curr = ["USD"] + new_curr
                extr.append([el, cycle_val(new_curr)])
    else:
        new_curr = ['USD', 'CAD', 'GBP', 'AUD', 'JPY', 'CHF', 'EUR']
        extr = cycle_val(new_curr)

    df = pd.DataFrame(extr, columns=["cycle", "val"])
    df = df.sort_values(by="val", ascending=False)
    df.to_csv("./currency_csv.csv")
    print(df.values)

if __name__=="__main__":
    # debug = False
    main()
    # print('Hi')