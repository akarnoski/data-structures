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
        stack = Stack()
        curr = self.root
        ready = True
        while ready:
            if curr:
                stack.push(curr)
                curr = curr.left
            else:
                if len(stack) != 0:
                    curr = stack.pop()
                    yield curr.val
                    curr = curr.right
                else:
                    ready = False

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
        stack = Stack()
        curr = self.root
        ready = True
        while ready:
            if curr:
                stack.push(curr)
                curr = curr.left
            else:
                out = stack.pop()
                print(out.val)
                if out.left is None and out.right is None:
                    order_list.append(out.val)
                if out.left:
                    if out.left.val in order_list and out.right:
                        order_list.append(out.right.val)
                if len(stack) == 0:
                    ready = False
                    return order_list
     
    # def breadth_first(self):
    #     """Traverse binary seach tree using breadth first traversal."""
    #     q = Queue()
    #     curr = self.root
    #     q.enqueue(curr.val)
    #     while len(q) != 0:

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
            print(delete_node.val)
        curr = delete_node
        if curr.right and curr.left:
            curr = curr.left
            if curr.right:
                curr = curr.right
                while curr.right:
                    curr = curr.right
                print('right: {}'.format(curr.val))
            else:
                curr = curr.left
                while curr.left:
                    curr = curr.left
                print('left: {}'.format(curr.val))


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(15)
    bst.insert(23)
    bst.insert(13)
    bst.insert(10)
    bst.insert(7)
    bst.insert(18)
    bst.insert(30)
    bst.insert(5)
    bst.insert(9)
    bst.insert(17)
    bst.insert(27)
