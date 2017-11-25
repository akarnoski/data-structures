"""Create a Binary Search Tree."""


class Node(object):
    """Build a node object."""

    def __init__(self, val=None):
        """Constructor for the Node object."""
        self.val = val
        self.left = None
        self.right = None
        self.depth = 0


class BinarySearchTree(object):
    """Build binary search tree object."""

    def __init__(self, iterable=()):
        """Constructor for the Linked List object."""
        self.root = None
        self._stats = {
            'counter': 0,
            'tree_depth': 0,
            'left_depth': 0,
            'right_depth': 0
        }
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.insert(item)

    def insert(self, val):
        """Insert val into binary search tree."""
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            self._stats['counter'] += 1
            return
        curr = self.root
        while curr:
            if new_node.val > curr.val:
                if curr.right is None:
                    new_node.depth += 1
                    self.adjust_stats(new_node)
                    curr.right = new_node
                    break
                new_node.depth += 1
                curr = curr.right
            if new_node.val < curr.val:
                if curr.left is None:
                    new_node.depth += 1
                    self.adjust_stats(new_node)
                    curr.left = new_node
                    break
                new_node.depth += 1
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

    def depth(self):
        """Return the depth of the binary search tree."""
        return self._stats['tree_depth']

    def size(self):
        """Return size of binary search tree."""
        return self._stats['counter']

    def contains(self, val):
        """Return true if binary search tree contains value."""
        return bool(self.search(val))

    def balance(self):
        """Get the balance of the binary search tree."""
        return self._stats['left_depth'] - self._stats['right_depth']

    def adjust_stats(self, node):
        """Function to make adjustments to dictionary attached to bst."""
        self._stats['counter'] += 1
        current_depth = self._stats['tree_depth']
        new_depth = node.depth
        if new_depth > current_depth:
            self._stats['tree_depth'] = new_depth
        if node.val < self.root.val:
            if new_depth > self._stats['left_depth']:
                self._stats['left_depth'] = new_depth
        if node.val > self.root.val:
            if new_depth > self._stats['right_depth']:
                self._stats['right_depth'] = new_depth