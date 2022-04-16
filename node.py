class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.data)