"""Make a Queue object that has access to DoublyLinkedList methods."""
from doubly_linked_list import DoublyLinkedList


class Queue(object):
    """Create a Queue object."""

    def __init__(self):
        """Initialize Queue using DoublyLinkedList methods."""
        self.doubly_linked_list = DoublyLinkedList()

    def enqueue(self, val):
        """Add a node to queue."""
        self.doubly_linked_list.push(val)

    def dequeue(self):
        """Remove first node pushed in."""
        try:
            return self.doubly_linked_list.shift()
        except IndexError:
            raise IndexError('Nothing to dequeue')
