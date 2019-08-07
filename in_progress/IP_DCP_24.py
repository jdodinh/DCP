"""
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or
ancestors are not locked.

Design a binary tree node class with the following methods:
    - is_locked, which returns whether the node is locked
    - lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should
    lock it and return true.
    - unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock
    it and return true.

You may augment the node to add parent pointers or any other property you would like. You may assume the class is used
in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h
is the height of the tree.
"""


class tree_node():
    def __init__(self, right, left, parent, locked):
        self.right = right
        self.left = left
        self.parent = parent
        self.locked = None

    def is_locked(self):
        ancestor = self.parent()
        while ancestor.locked is True and ancestor is not None:
            ancestor = ancestor.parent()
            if ancestor.locked is False: return False
        
