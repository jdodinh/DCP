"""
Given the root to a binary search tree, find the second largest node in the tree.
"""


class Node:                                                     # Creating a Node object, includes left, right and parent pointers
    def __init__(self, right, left, parent, val: int):          # Parent pointers are not necessary in this version of implementation
        self.right = right
        self.left = left
        self.parent = parent
        self.val = val


def init_tree():                                                # Initializing an arbitrary BST
    root = Node(right=None, left=None, parent=None,  val=5)
    one = Node(right=None, left=None, parent=None,  val=1)
    two = Node(right=None, left=None, parent=None,  val=2)
    three = Node(right=None, left=None, parent=None,  val=3)
    four = Node(right=None, left=None, parent=None,  val=4)
    six = Node(right=None, left=None, parent=None,  val=6)
    seven = Node(right=None, left=None, parent=None,  val=7)
    eight = Node(right=None, left=None, parent=None,  val=8)
    ten = Node(right=None, left=None, parent=None,  val=10)
    nine = Node(right=None, left=None, parent=None,  val=9)
    root.left = three
    three.parent = root
    root.right = ten
    ten.parent = root
    three.left = two
    two.parent = three
    three.right = four
    four.parent = three
    two.left = one
    one.parent = two
    ten.left = seven
    seven.parent = ten
    seven.left = six
    six.parent = seven
    seven.right = eight
    eight.parent = seven
    eight.right = nine
    nine.parent = eight

    return root


def find_2nd_smallest(root: Node):                              # Function that find the second largest, given root of the tree
    v = root                                                    # We start off by finding the rightmost node in the tree, thus the largest node.
    while v.right.right is not None:                            # The second largest node is the largest node in its left subtree. 
        v = v.right
    if v.right.left is None:                                    # At this point v.right is the largest node in the tree. If it doesn't have a left 
        return v                                                # child, the second largest node is v (v.right's parent)
    if v.right.left.right is None:                              # If the largest node's left child doesnt have a right child, the second largest 
        return v.right.left                                     # node is that left child
    v = v.right.left                                            # else we find the largest node in the left subtree of the largest node in the tree
    while v.right is not None:
        v = v.right
    return v.val                                                # return the value


def main():
    root = init_tree()                                          # Initialize tree
    val = find_2nd_smallest(root)                               # Find second largest node
    print(val)                                                  # Print Value


if __name__ == "__main__":
    main()
