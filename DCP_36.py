"""
Given the root to a binary search tree, find the second largest node in the tree.
"""


class Node:
    def __init__(self, right, left, parent, val: int):
        self.right = right
        self.left = left
        self.parent = parent
        self.val = val


def init_tree():
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


def find_2nd_smallest(root: Node):
    v = root
    while v.right.right is not None:
        v = v.right
    if v.right.left is None:
        return v
    if v.right.left.right is None:
        return v.right.left
    v = v.right.left
    while v.right is not None:
        v = v.right
    return v.val


def main():
    root = init_tree()
    val = find_2nd_smallest(root)
    print(val)


if __name__ == "__main__":
    main()
