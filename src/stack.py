"""Make a new Stack object that has access to LinkedList methods."""
from linked_list import LinkedList


class Stack(object):
    """Create a Stack object."""

    def __init__(self):
        """Initialize new Stacks with access to LinkedList methods."""
        self.linked_list = LinkedList()

    def push(self, val):
        """Push a thing onto a thing."""
        self.linked_list.push(val)

    def pop(self):
        """Pop a thing out of the thing."""
        try:
            return self.linked_list.pop()
        except IndexError:
            IndexError('Cannot pop from empty stack')

    def __len__(self):
        """Return the list of the stack."""
        return self.linked_list.size()
