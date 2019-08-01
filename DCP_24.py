
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
        
