"""
You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where
N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or
diagonal.
"""
############################################################################
# My solution explores a tree, where each node has a coordinate (except the root node), and an array of options, which
# define the fields on which queens can be placed. A path down such tree, will thus represent a way of placing queens
# such that they don't threaten each other. Each node also has a level attribute signifying its depth. As soon as a
# level N node is reached, we know that using this path it's possible to place 9 queens, as there are 9 nodes on the
# path from the root to that particular node.
# Finally the function create children, creates an array of TreeNode objects corresponding to that particular node, such
# that the options include only the fields on which a queen can be placed.
# Back tracking is implemented with the use of a stack, where only the latest visited nodes, with non empty options can
# exist


class TreeNode:                                        # TreeNode class
    def __init__(self, level, rem_options, coord):
        self.level = level                              # The level of the node represents the number of queens placed.
        self.options = []                               # The variable that holds the fields where the next queen can be placed
        self.children = []                              # array of TreeNode objects
        self.coord = coord                              # Coordinate of particular TreeNode object
        self.rem_opt = rem_options                      # The remaining options on the chessboard available
        if self.rem_opt:                                # creating the possibilities of the next move
            el = self.rem_opt[0]                        # removing all coordinates in the next column from the node, and appending to current options
            if el[1] == self.level:                     # level signifies the column of the chessboard in which we wish
                while el[1] == self.level:              # to place the next queen safely. We remove it from the overall
                    self.options.append(self.rem_opt.pop(0)) # list of options, and place it in the current list that is
                    if self.rem_opt:                    #  being inspected.
                        el = self.rem_opt[0]
                    else:
                        break
        else:
            pass
        # self.next = next_options
        # self.exhausted = []

    def create_children(self):

        for co in self.options:
            opt = self.rem_opt.copy()
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
    boxes_master = []
    start = []
    count = 0
    N = 11
    for j in range(N):
        for i in range(N):
            boxes_master.append((i, j))         # Creating the array of all chessboard coordinates.
    root = TreeNode(0, boxes_master, None)      # creating the root of the tree, containing the options, with Level == 0
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
