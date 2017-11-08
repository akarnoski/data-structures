"""Create a new Node object and attach it a Linked List."""


class Node(object):
    """Build a node object."""

    def __init__(self, data=None, next=None):
        """Constructor for the Node object."""
        self.data = data
        self.next = next

    def __str__(self):
        """."""
        return "Node {}".format(self.data)


class LinkedList(object):
    """Build linked list."""

    def __init__(self, iterable=()):
        """Constructor for the Linked List object."""
        self.head = None
        self._counter = 0
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.push(item)

    def push(self, val):
        """Add a new value to the head of the Linked List."""
        new_head = Node(val, self.head)
        self.head = new_head
        self._counter += 1

    def pop(self):
        """Remove and return the value if the head of the Linked List."""
        if not self.head:
            raise IndexError("Empty list, unable to pop")
        output = self.head.data
        self.head = self.head.next
        self._counter -= 1
        return output

    def size(self):
        """Return size of our list."""
        return self._counter

    def search(self, val):
        """Search linked list for requested node."""
        search_through = self.head
        while search_through:
            if val == search_through.data:
                return search_through
            else:
                search_through = search_through.next
        return search_through

    def remove(self, val):
        """Remove selected node."""
        current_node = self.head
        previous_node = None
        found = False
        if current_node is None:
            return ValueError("No such item.")
        while current_node or found is False:
            if val == current_node.data:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.next
        if previous_node is None:
            self.pop()
        elif current_node.next is None:
            previous_node.next = None
        else:
            previous_node.next = current_node.next

    def display(self):
        """Display nodes in linked list."""
        node = self.head
        display_this = []
        while node:
            display_this.append(node.data)
            node = node.next
        return str(display_this).replace("[", "(").replace("]", ")")

    def __len__(self):
        """Return length of linked list."""
        return self.size()

    def __str__(self):
        """Display the linked list."""
        return self.display()
