"""Test functions for deque module."""
import pytest


def test_queue_is_instance_of_queue_object():
    """Test stack is instance of Stack()."""
    from deque import Deque
    d = Deque()
    assert isinstance(d, Deque)


def test_queue_is_instance_of_doubly_linked_list():
    """Test stack inherits from DoublyLinkedList."""
    from deque import Deque
    from doubly_linked_list import DoublyLinkedList
    d = Deque()
    assert isinstance(d._doubly_linked_list, DoublyLinkedList)


def test_enqueue_adds_a_value(deque_fixture):
    """Test the enqueue method adds value."""
    deque_fixture.append(2)
    assert deque_fixture._doubly_linked_list.tail.data == 2


# def test_append_adds_multiple_values_and_checks_front(deque_fixture):
#     """Test the append method adds value."""
#     deque_fixture.append(2)
#     deque_fixture.append(3)
#     assert deque_fixture._doubly_linked_list.tail.data == 2


# def test_dequeue_removes_first_node_added(deque_fixture):
#     """Test that node dequeued is first node added."""
#     deque_fixture.append(2)
#     remove = deque_fixture.popleft()
#     assert remove == 2


# def test_popleft_removes_first_node_added_even_with_multiple_nodes(deque_fixture):
#     """Test that node popleftd is first node added even with multiple nodes."""
#     deque_fixture.append(2)
#     deque_fixture.append(3)
#     remove = deque_fixture.popleft()
#     assert remove == 2