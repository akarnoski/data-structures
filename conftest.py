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
