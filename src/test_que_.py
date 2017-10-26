import pytest


def test_queue_is_instance_of_queue_object():
    """Test stack is instance of Stack()."""
    from que_ import Queue
    q = Queue()
    assert isinstance(q, Queue)


def test_queue_is_instance_of_doubly_linked_list():
    """Test stack inherits from DoublyLinkedList."""
    from que_ import Queue
    from doubly_linked_list import DoublyLinkedList
    q = Queue()
    assert isinstance(q.doubly_linked_list, DoublyLinkedList)
