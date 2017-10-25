"""Build a Doubly Linked list object."""


class Node(object):
    """Create a new Node object."""

    def __init__(self, data=None, next_node=None, previous_node=None):
        """Initialized values of new Node object."""
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node


class DoublyLinkedList(object):
    """Create a Doubly Linked List."""

    def __init__(self):
        """Initialized value of new Double Linked List object."""
        self.head = None
        self._counter = 0

    def push(self, val):
        """Add a new value to the head and tail of the Doubly Linked List."""
        new_head = Node(val, self.head)
        if self.head:
            self.head.previous_node = new_head
        self.head = new_head
        self._counter += 1
