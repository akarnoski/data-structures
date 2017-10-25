"""."""


class Node(object):

    def __init__(self, data=None, next=None):
        """Constructor for the Node object."""
        self.data = data
        self.next = next

    def __str__(self):
        """."""
        return "Node {}".format(self.val)


class LinkedList(object):

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
        """Removes and return the value if the head of the Linked List."""
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
        """."""
        curr = self.head
        while curr:
            if curr.data == val:
                return curr
            curr = curr.next

    def remove(self, node):
        """."""
        current = self.head
        while current:
            print(current.val, node)
            if current.val == node:
                print('right here')
                self.remove(node)
            else:
                current = current.next

    def display(self):
        """."""
        node = self.head
        while node:
            print('node: {}'.format(node.val))
            node = node.next

    def __len__(self):
        """."""
        return self._counter

    def __print__(self):
        """."""
        pass
