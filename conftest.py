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
