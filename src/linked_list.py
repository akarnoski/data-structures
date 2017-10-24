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

    popped = 0

    node_list = []

    def push(self, val):
        """."""
        self.node_list.insert(0, Node(val))

    def pop(self):
        """."""
        self.popped = self.node_list.pop(0)
        print(self.popped)

    def size(self):
        """."""
        return len(self.node_list)

    def search(self, val):
        """."""
        for i in range(len(self.node_list)):
            if val == self.node_list[i].val:
                print(self.node_list[i])

    def remove(self, node):
        """."""
        pass

    def display(self):
        """."""
        pass

    def __len__(self):
        """."""
        return len(self.node_list)

    def __print__(self):
        """."""
        pass
