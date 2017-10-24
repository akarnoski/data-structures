"""."""


class Node(object):
    """."""

    def __init__(self, val=None, next=None):
        """."""
        self.val = val
        self.next = next

    def __str__(self):
        """."""
        return "Node {}".format(self.val)


class LinkedList(object):
    """."""

    def __init__(self, optional=None, head=None):
        self.optional = optional
        self.head = head

        if self.optional is not None:
            return "{}".format(self.optional)

    node_list = []

    def push(self, val):
        """."""
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """."""
        node = self.head
        if node:
            self.head = self.head.next
            print('yes')
        if node is None:
            raise IndexError("Nothing to remove from list.")

    def size(self):
        """."""
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def search(self, val):
        """."""
        node = self.head
        while node:
            if node.val == val:
                return node.val
            else:
                node = node.next

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
        return self.length

    def __print__(self):
        """."""
        pass




l = LinkedList()
for i in range(10):
    l.push(i)