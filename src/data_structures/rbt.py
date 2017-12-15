"""Building a red black search tree."""
from que_ import Queue


class Node(object):
    """Build a node object."""

    def __init__(self, val=None):
        """Constructor for the Node object."""
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.red = True
        self.black_height = 0


class RedBlackTree(object):
    """Build a red black tree object."""

    def __init__(self, iterable=()):
        """Constructor for the red black tree object."""
        self.root = None
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.insert(item)

    def insert(self, val):
        """Insert val into red black tree."""
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            new_node.red = False
            return
        curr = self.root
        while curr:
            if new_node.val > curr.val:
                if curr.right is None:
                    new_node.parent = curr
                    curr.right = new_node
                    break
                curr = curr.right
            if new_node.val < curr.val:
                if curr.left is None:
                    new_node.parent = curr
                    curr.left = new_node
                    break
                curr = curr.left
        self.make_family(new_node)

    def _black_node_depth(self, depth):
        """."""

    def make_family(self, node):
        """Make a list of family members for node."""
        family = Queue()
        family.enqueue(node)
        if node.parent:
            family.enqueue(node.parent)
        if node.parent.parent:
            parent = node.parent
            grandparent = node.parent.parent
            family.enqueue(grandparent)
            if grandparent.left:
                if grandparent.left != parent:
                    family.enqueue(grandparent.left)
            if grandparent.right:
                if grandparent.right != parent:
                    family.enqueue(grandparent.right)
        self.recoloring(family)

    def recoloring(self, family):
        """Perform recoloring on node family."""
        if len(family) is 2:
            node = family.dequeue()
            parent = family.dequeue()
            if parent.red is True:
                node.red = False
        if len(family) is 3:
            node = family.dequeue()
            node.red = False
            parent = family.dequeue()
            grandparent = family.dequeue()
            node.red = False
        if len(family) is 4:
            node = family.dequeue()
            parent = family.dequeue()
            grandparent = family.dequeue()
            uncle = family.dequeue()
            if uncle.red is True and parent.red is True:
                parent.red = False
                uncle.red = False
            else:
                if 






if __name__ == '__main__':
    rbt = RedBlackTree()
    rbt.insert(15)
    # rbt.insert(23)
    rbt.insert(7)
    rbt.insert(5)
    # rbt.insert(10)
    # rbt.insert(17)
    # rbt.insert(27)
