"""Create a Binary Search Tree."""


class Node(object):
    """Build a node object."""

    def __init__(self, val=None, left=None, right=None):
        """Constructor for the Node object."""
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree(object):
    """Build binary search tree object."""

    def __init__(self, iterable=()):
        """Constructor for the Linked List object."""
        self.root = None
        self._counter = 0
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.insert(item)

    def insert(self, val):
        """Insert val into binary search tree."""
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            self._counter += 1
            return
        curr = self.root
        while curr:
            if new_node.val > curr.val:
                if curr.right is None:
                    curr.right = new_node
                    self._counter += 1
                    break
                curr = curr.right
            if new_node.val < curr.val:
                if curr.left is None:
                    curr.left = new_node
                    self._counter += 1
                    break
                curr = curr.left

    def search(self, val):
        """Search binary search tree for value."""
        try:
            curr = self.root
            while curr:
                if curr.val is val:
                    return curr
                if curr.val < val:
                    if curr.right is None:
                        return
                    curr = curr.right
                if curr.val > val:
                    if curr.left is None:
                        return
                    curr = curr.left
        except IndexError:
            raise IndexError('No nodes to search.')

    def size(self):
        """Return size of binary search tree."""
        return self._counter

    def contains(self, val):
        """Return true if binary search tree contains value."""
        try:
            curr = self.root
            while curr:
                if curr.val is val:
                    return True
                if val > curr.val:
                    if curr.right is None:
                        return False
                    curr = curr.right
                if val < curr.val:
                    if curr.left is None:
                        return False
                    curr = curr.left
        except IndexError:
            raise IndexError('No nodes to search.')

    def balance(self):
        """Return integar representing balance of binary search tree."""
        try:
            left_side = 0
            right_side = 0
            if self._counter == 1:
                return 0
            curr = self.root
            if curr.left:
                left_branch = curr.left
            if curr.right:
                right_branch = curr.right
            left_branch = None
            right_branch = None
            while curr:
                if self.root is node:
                    return node
                if node.val > curr.val:
                    if curr.right is None:
                        return
                    curr = curr.right
                if node.val < curr.val:
                    if curr.left is None:
                        return
                    curr = curr.left
        except IndexError:
            raise IndexError('No nodes to search.')

