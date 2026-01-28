class Node:
    def __init__(self, value):
        self.value = value
        self.children = [] # For general tree (Bonus)
    
    @property
    def left(self):
        if len(self.children) > 0:
            return self.children[0]
        return None
    
    @left.setter
    def left(self, node):
        if len(self.children) == 0:
            self.children.append(node)
        else:
            self.children[0] = node

    @property
    def right(self):
        if len(self.children) > 1:
            return self.children[1]
        return None
    
    @right.setter
    def right(self, node):
        while len(self.children) < 2:
            self.children.append(None)
        self.children[1] = node

    def add_child(self, node):
        """Helper for general tree bonus"""
        self.children.append(node)
