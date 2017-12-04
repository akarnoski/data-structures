"""Create a trie tree."""


class Node(object):
    """Build a node object."""

    def __init__(self, val=None):
        """Constructor for the Node object."""
        self.val = val
        self.parent = None
        self.children = {}


class TrieTree(object):
    """Create a trie tree object."""

    def __init__(self):
        """Constructor for the trie tree object."""
        self.size = 0
        self.root = Node('*')

    def insert(self, string):
        """Insert string into trie tree."""
        curr = self.root
        string = string + '$'
        for letter in string:
            print(letter)
            if letter in curr.children:
                curr = curr.children[letter]
                new = False
            else:
                new_letter = Node(letter)
                new_letter.parent = curr
                curr.children[letter] = new_letter
                curr = new_letter
                new = True
        if new:
            self.size += 1

    def size(self):
        """Return size of trie tree."""
        return self.size

    def contains(self, string):
        """Return true if string is in trie."""
        try:
            self._node_crawler(string)
            return True
        except KeyError:
            return False

    def _val_crawler(self, string):
        """Trie tree crawler helper function that returns values of the nodes
        to help me visualize while testing."""
        values = []
        curr = self.root
        values.append(curr.val)
        string = string + '$'
        try:
            for letter in string:
                curr = curr.children[letter]
                values.append(curr.val)
        except KeyError:
            raise KeyError('Word not in Trie Tree')
        return values

    def _node_crawler(self, string):
        """Trie tree crawler helper function that returns list of the nodes
        to help me visualize while testing."""
        nodes = []
        curr = self.root
        nodes.append(curr)
        string = string + '$'
        try:
            for letter in string:
                curr = curr.children[letter]
                nodes.append(curr)
        except KeyError:
            raise KeyError('Word not in Trie Tree')
        return nodes
