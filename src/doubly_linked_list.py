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
        new_tail = Node(val, self.tail)
        if self.tail:
            self.tail.next_node = new_tail
        else:
            self.head = new_tail
        self.tail = new_tail
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
            raise IndexError("Empty list, unable to pop")
        output = self.tail.data
        self.tail = self.tail.previous_node
        self._counter -= 1
        return output

    def display(self):
        """Display nodes in linked list."""
        node = self.head
        display_this = []
        while node:
            display_this.append(node.data)
            node = node.next_node
        return str(display_this).replace("[", "(").replace("]", ")")

    def size(self):
        """Return size of our list."""
        return self._counter

    def __len__(self):
        """Return length of linked list."""
        return self.size()

    def __str__(self):
        """Allowed the DLL to use the Python print function to display list."""
        return self.display()
