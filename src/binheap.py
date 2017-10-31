"""Build a binary heap object."""


class Node(object):
    """Build a node object."""

    def __init__(self, data=None, parent=None, left_child=None, right_child=None):
        """Constructor for the Node object."""
        self.data = data
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child


class BinHeap(object):
    """Construct a Binary Heap object."""

    def __init__(self):
        """Initialized value of Binary Heap object."""
        self.heap = []

    def push(self, val):
        """Add a new Node to the Binary Heap."""
        # new_node = Node(val)
        self.heap.append(val)
        if self.heap != sorted(self.heap, reverse=True):
            self.heap = sorted(self.heap, reverse=True)
