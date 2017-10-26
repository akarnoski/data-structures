"""Make a Queue object that has access to DoublyLinkedList methods."""
from doubly_linked_list import DoublyLinkedList


class Queue(object):
    """Create a Queue object."""

    def __init__(self):
        """Initialize Queue using DoublyLinkedList methods."""
        self.doubly_linked_list = DoublyLinkedList()
