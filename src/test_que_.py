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


def test_enqueue_adds_a_value(queue_fixture):
    """Test the enqueue method adds value."""
    queue_fixture.enqueue(2)
    assert queue_fixture.doubly_linked_list.head.data == 2


def test_enqueue_adds_multiple_values_and_checks_front(queue_fixture):
    """Test the enqueue method adds value."""
    queue_fixture.enqueue(2)
    queue_fixture.enqueue(3)
    assert queue_fixture.doubly_linked_list.tail.data == 2
