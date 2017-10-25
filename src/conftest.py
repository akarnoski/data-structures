"""pytest fixture."""
import pytest


@pytest.fixture
def list_fixture():
    from linked_list import LinkedList
    l = LinkedList()


@pytest.fixture
def dll_fixture():
    from double_linked_list import DoubleLinkedList
    dll = LinkedList()