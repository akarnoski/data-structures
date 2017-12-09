"""pytest fixture."""
import pytest


@pytest.fixture
def list_fixture():
    from linked_list import LinkedList
    l = LinkedList()
    return l


@pytest.fixture
def dll_fixture():
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    return dll


@pytest.fixture
def queue_fixture():
    from que_ import Queue
    q = Queue()
    return q


@pytest.fixture
def deque_fixture():
    from deque import Deque
    d = Deque()
    return d


@pytest.fixture
def bh_fixture():
    from binheap import BinaryHeap
    b = BinaryHeap()
    return b


@pytest.fixture
def graph_fixture():
    from graph import Graph
    g = Graph()
    return g


@pytest.fixture
def bst_fixture():
    from bst import BinarySearchTree
    bst = BinarySearchTree()
    return bst


@pytest.fixture
def ht_fixture():
    from hash_table import HashTable
    ht = HashTable(20)
    return ht

@pytest.fixture
def tt_fixture():
    from trie_tree import TrieTree
    tt = TrieTree()
    return tt