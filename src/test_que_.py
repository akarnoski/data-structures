"""Test functions for que_ module."""
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
    assert isinstance(q._doubly_linked_list, DoublyLinkedList)


def test_enqueue_adds_a_value(queue_fixture):
    """Test the enqueue method adds value."""
    queue_fixture.enqueue(2)
    assert queue_fixture._doubly_linked_list.head.data == 2


def test_enqueue_adds_multiple_values_and_checks_front(queue_fixture):
    """Test the enqueue method adds value."""
    queue_fixture.enqueue(2)
    queue_fixture.enqueue(3)
    assert queue_fixture._doubly_linked_list.tail.data == 2


def test_dequeue_removes_first_node_added(queue_fixture):
    """Test that node dequeued is first node added."""
    queue_fixture.enqueue(2)
    remove = queue_fixture.dequeue()
    assert remove == 2


def test_dequeue_removes_first_node_added_even_with_multiple_nodes(queue_fixture):
    """Test that node dequeued is first node added even with multiple nodes."""
    queue_fixture.enqueue(2)
    queue_fixture.enqueue(3)
    remove = queue_fixture.dequeue()
    assert remove == 2


def test_dequeue_raises_exception_on_empty_queue(queue_fixture):
    """Test that index error is raised when dequeuing empty queue."""
    with pytest.raises(IndexError):
        queue_fixture.dequeue()


def test_peek_returns_next_value_to_be_dequeued(queue_fixture):
    """Test that value returned is from node next to be dequeued."""
    queue_fixture.enqueue(2)
    assert queue_fixture.peek() == 2


def test_peek_returns_none_on_empty_queue(queue_fixture):
    """Test that None is returned on empty list peek."""
    assert queue_fixture.peek() is None


def test_size_method_returns_list_length_0_if_empty(queue_fixture):
    """Test size method returns 0 on empty queue."""
    assert queue_fixture.size() == 0


def test_size_method_returns_list_length(queue_fixture):
    """Test size method on queue."""
    queue_fixture.enqueue(2)
    queue_fixture.enqueue(3)
    assert queue_fixture.size() == 2


def test_python_len_function_works_with_queue(queue_fixture):
    """Test that queue works with len function."""
    assert len(queue_fixture) == 0
