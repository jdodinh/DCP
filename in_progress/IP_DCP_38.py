"""
You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where
N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or
diagonal.
"""
############################################################################
# My solution explores a tree, where each node has a coordinate (except the root node), and an array of options, which
# define the fields on which queens can be placed. A path down such tree, will thus represent a way of placing queens
# such that they don't threaten eachother. Each node also has a level attribute signifying its depth. As soon as a level
# N node is reached, we know that using this path it's possible to place 9 queens, as there are 9 nodes on the path from
# the root to that particular node.
# Finally the function create children, creates an array of TreeNode objects corresponding to that particular node, such
# that the options include only the fields on which a queen can be placed.
# Back tracking is implemented with the use of a stack, where only the latest visited nodes, with non empty options can
# exist

import math


class TreeNode():                                   # TreeNode classs
    def __init__(self, level, options, coord):
        self.level = level
        self.options = options
        self.children = []
        self.coord = coord
        # self.exhausted = []

    def create_children(self):
        for co in self.options:
            opt = []
            for el in self.options:
                opt.append((el[0], el[1]+1))
            # opt.remove(co)
            self.children.append(TreeNode(self.level+1, array_filter(opt, co), co))


def array_filter(arr: list, coord: tuple):
    row = coord[0]
    col = coord[1]
    filter_arr = arr.copy()
    for el in arr:
        r = el[0]
        c = el[1]
        if r == row or c == col or (r-c) == (row - col) or (r+c) == (row+col):
            filter_arr.remove(el)
    return filter_arr


def main():
    count = 0
    N = 4
    boxes = []
    for i in range(N):
        boxes.append((i, 0))
    root = TreeNode(0, boxes, None)
    root.create_children()
    queue = root.children.copy()
    while queue:
        node = queue.pop()
        if node.level == N-1 and node.options:
            count += 1
            continue
        node.create_children()
        queue = queue + node.children

    print(count)


if __name__ == "__main__":
    main()
