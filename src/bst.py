"""Create a Binary Search Tree."""
from stack import Stack
from que_ import Queue


class Node(object):
    """Build a node object."""

    def __init__(self, val=None):
        """Constructor for the Node object."""
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.color = None
        self.depth = 0


class BinarySearchTree(object):
    """Build binary search tree object."""

    def __init__(self, iterable=()):
        """Constructor for the binary search tree object."""
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
                    new_node.parent = curr
                    curr.right = new_node
                    break
                new_node.depth += 1
                curr = curr.right
            if new_node.val < curr.val:
                if curr.left is None:
                    new_node.depth += 1
                    self.adjust_stats(new_node)
                    new_node.parent = curr
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

    def in_order(self):
        """Traverse the binary search tree in order."""
        stack = []
        curr = self.root
        ready = True
        while ready:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                if len(stack) != 0:
                    curr = stack.pop()
                    yield curr.val
                    curr = curr.right
                else:
                    break

    def pre_order(self):
        """Traverse the binary search tree pre order."""
        order_list = []
        stack = Stack()
        curr = self.root
        ready = True
        while ready:
            if curr:
                stack.push(curr)
                if curr not in order_list:
                    order_list.append(curr.val)
                curr = curr.left
            else:
                if len(stack) != 0:
                    curr = stack.pop()
                    curr = curr.right
                else:
                    ready = False
        for value in order_list:
            yield value

    def post_order(self):
        """Traverse the binary search tree post order."""
        order_list = []
        q = Queue()
        curr = self.root
        q.enqueue(curr)
        while len(q) != 0:
            curr = q.dequeue()
            if curr.right:
                q.enqueue(curr.right)
            if curr.left:
                q.enqueue(curr.left)
            order_list.append(curr.val)
        return order_list[::-1]

    def breadth_first(self):
        """Traverse binary seach tree using breadth first traversal."""
        q = Queue()
        curr = self.root
        q.enqueue(curr)
        while len(q) != 0:
            curr = q.dequeue()
            if curr.left:
                q.enqueue(curr.left)
            if curr.right:
                q.enqueue(curr.right)
            yield curr.val

    def get_node(self, val):
        """Helped function to get node on the tree."""
        curr = self.root
        while curr:
            if curr.val is val:
                return curr
            if curr.val < val:
                curr = curr.right
            if curr.val > val:
                curr = curr.left

    def delete(self, val):
        """Delete node from binary search tree."""
        if self.search(val):
            delete_node = self.get_node(val)
        curr = delete_node
        if curr.right is None and curr.left is None:
            if curr.val == self.root.val:
                self.root = None
                return
            parent = curr.parent
            if curr.val > parent.val:
                parent.right = None
            else:
                parent.left = None
        if curr.right and curr.left is None:
            child = curr.right
            parent = curr.parent
            if curr.val == parent.left.val:
                parent.left = child
            if curr.val == parent.right.val:
                parent.right = child
        if curr.left and curr.right is None:
            child = curr.left
            parent = curr.parent
            if curr.val == parent.left.val:
                parent.left = child
            if curr.val == parent.right.val:
                parent.right = child
        if curr.right and curr.left:
            parent = delete_node.parent
            curr = curr.left
            if curr.right:
                while curr.right:
                    curr = curr.right
            swap_node = curr
            swap_node.left = delete_node.left
            swap_node.left.parent = swap_node
            swap_node.right = delete_node.right
            swap_node.right.parent = swap_node
            if parent.right.val == delete_node.val:
                parent.right = swap_node
            if parent.left.val == delete_node.val:
                parent.left = swap_node


