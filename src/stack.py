"""."""
from linked_list import LinkedList


class Stack(object):
    """Create a Stack object."""

    def __init__(self):
        """."""
        self.linked_list = LinkedList()

    def push(self, val):
        """Push a thing onto a thing."""
        self.linked_list.push(val)

    def pop(self):
        """."""
        return self.linked_list.pop()

    def __len__(self):
        """."""
        return self.linked_list.size()
