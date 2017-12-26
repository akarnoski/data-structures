"""Make a Queue object that has access to DoublyLinkedList methods."""
from doubly_linked_list import DoublyLinkedList


class Queue(object):
    """Create a Queue object."""

    def __init__(self):
        """Initialize Queue using DoublyLinkedList methods."""
        self._doubly_linked_list = DoublyLinkedList()

    def enqueue(self, val):
        """Add a node to queue."""
        self._doubly_linked_list.push(val)

    def dequeue(self):
        """Remove first node pushed in."""
        try:
            return self._doubly_linked_list.shift()
        except IndexError:
            raise IndexError('Nothing to dequeue')

    def peek(self):
        """Get value of next node to be dequeued."""
        if self._doubly_linked_list.size() == 0:
            return None
        return self._doubly_linked_list.tail.data

    def size(self):
        """Get the size of the queue."""
        return self._doubly_linked_list.size()

    def __len__(self):
        """Return the length of the queue using Python len function."""
        return self.size()
