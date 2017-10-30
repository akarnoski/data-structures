"""Make a Deque object that has access to DoublyLinkedList methods."""
from doubly_linked_list import DoublyLinkedList


class Deque(object):
    """Create a Deque object."""

    def __init__(self):
        """Initialize Deque using DoublyLinkedList methods."""
        self._doubly_linked_list = DoublyLinkedList()

    def append(self, val):
        """Add a node to back Deque."""
        self._doubly_linked_list.append(val)

    def appendleft(self, val):
        """Add a node to front Deque."""
        self._doubly_linked_list.push(val)

    def pop(self):
        """Remove node at the back."""
        try:
            return self._doubly_linked_list.shift()
        except IndexError:
            raise IndexError('Nothing to pop')

    def popleft(self):
        """Remove node at the front."""
        try:
            return self._doubly_linked_list.pop()
        except IndexError:
            raise IndexError('Nothing to pop from front')

    def peek(self):
        """Get value of next node to be popped left."""
        if self._doubly_linked_list.size() == 0:
            return None
        return self._doubly_linked_list.tail.data

    def peekleft(self):
        """Get value of next node to be popped."""
        if self._doubly_linked_list.size() == 0:
            return None
        return self._doubly_linked_list.head.data

    def size(self):
        """Get the size of the Deque."""
        return self._doubly_linked_list.size()

    def __len__(self):
        """Return the length of the Deque using Python len function."""
        return self.size()
