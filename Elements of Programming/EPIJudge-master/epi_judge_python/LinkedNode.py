class LinkedNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next
    def add_after(self, node):
        self.next = node.next
        node.next = self.next