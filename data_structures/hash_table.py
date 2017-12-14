"""Create a hash table."""


class Node(object):
    """Build a node object for mini linked list."""

    def __init__(self, key=None, val=None, next=None):
        """Constructor for the Node object."""
        self.key = key
        self.val = val
        self.next = next


class LinkedList(object):
    """Build mini linked list to use for collisions."""

    def __init__(self,):
        """Constructor for the mini Linked List object."""
        self.head = None

    def push(self, key, val):
        """Add a new value to the head of the Linked List."""
        new_head = Node(key, val, self.head)
        self.head = new_head

    def search(self, key):
        """Search linked list for requested node."""
        search_through = self.head
        while search_through:
            if key == search_through.key:
                return search_through
            else:
                search_through = search_through.next
        return search_through


class HashTable(object):
    """Create a hash table object."""

    def __init__(self, buckets=None):
        """Constructor for hash table."""
        self.table = []
        self.size = 0
        self.available = 0
        self.buckets = buckets
        if self.buckets:
            linked_list = LinkedList()
            for i in range(buckets):
                self.table.append(linked_list)
            self.available = self.buckets - self.size

    def set(self, key, val):
        """Set key and value."""
        hash_value = self._hash(key)
        index = hash_value % self.buckets
        self.table[index].push(key, val)

    def get(self, key):
        """Return the value stored with the given key."""
        index = self._index_helper(key)
        return self.table[index].search(key).val

    def _hash(self, key):
        """Hash the given key."""
        if isinstance(key, str):
            total_hash = 0
            for letter in key:
                total_hash += ord(letter)
            return total_hash
        else:
            raise TypeError("Key must be a string")

    def _index_helper(self, key):
        """Help function to return index of hashed key."""
        hashed_value = self._hash(key)
        index = hashed_value % self.buckets
        return index

    def _hash_key(self, hash_value):
        """Use hash to get bucket in table."""
        print('{}'.format(hash_value))
        return hash_value % self.buckets

    def __len__(self):
        """Return the length of the Deque using Python len function."""
        return self.buckets