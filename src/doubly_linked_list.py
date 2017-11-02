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
        self.tail = None
        self._counter = 0

    def push(self, val):
        """Add a new value to the head the Doubly Linked List."""
        new_head = Node(val, self.head)
        if self.head:
            self.head.previous_node = new_head
        if self.tail is None:
            self.tail = new_head
        self.head = new_head
        self._counter += 1

    def append(self, val):
        """Add a new value to the tail of the Doubly Linked List."""
        old_tail = self.tail
        new_tail = Node(val, self.tail)
        old_tail.next_node = new_tail
        self.tail = new_tail
        self.tail.next_node = None
        self.tail.previous_node = old_tail
        self._counter += 1

    def pop(self):
        """Remove and return the value of the head."""
        if len(self) == 0:
            self.head = None
            self.tail = None
        if not self.head:
            raise IndexError("Empty list, unable to pop")
        output = self.head.data
        self.head = self.head.next_node
        self._counter -= 1
        return output

    def shift(self):
        """Remove and return the value of the tail."""
        if len(self) == 0:
            self.head = None
            self.tail = None
        if not self.tail:
            raise IndexError("Empty list, unable to shift")
        output = self.tail.data
        self.tail = self.tail.previous_node
        self._counter -= 1
        return output

    def size(self):
        """Return size of our list."""
        return self._counter

    def __len__(self):
        """Return length of our list."""
        return self.size()
