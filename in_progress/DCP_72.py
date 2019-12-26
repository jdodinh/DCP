import pandas as pd


graph_string = "ABACA"
graph_edges = [(0, 1),
               (0, 2),
               (2, 3),
               (3, 4)]

graph_dict = {}


class gph_node():
    def __init__(self, value, index):
        self.neighbors = []
        self.val = value
        self.ind = index


def main():
    for i in range(len(graph_string)):
        if graph_string[i] not in graph_dict:
            graph_dict[graph_string[i]] = gph_node(graph_string[i], index=i)


if __name__=="__main__":
    main()