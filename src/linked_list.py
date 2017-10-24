"""."""


class Node(object):
    """."""

    def __init__(self, val=None, next=None):
        """."""
        self.val = val
        self.next = next

    def __str__(self):
        """."""
        return "Node {}".format(self.val)


class LinkedList(object):
    """."""

    popped = LinkedList.node_list.pop()

    node_list = []

    def push(self, val):
        """."""
        self.node_list.insert(0, Node(val))

    def pop(self):
        """."""
        self.pop()

    def size(self):
        """."""
        pass

    def search(self, val):
        """."""
        pass

    def remove(self, node):
        """."""
        pass

    def display(self):
        """."""
        pass

    def __len__(self):
        """."""
        pass

    def __print__(self):
        """."""
        pass
