"""Test functions for deque module."""
import pytest


def test_deque_is_instance_of_deque_object():
    """Test stack is instance of Stack()."""
    from deque import Deque
    d = Deque()
    assert isinstance(d, Deque)


def test_deque_is_instance_of_doubly_linked_list():
    """Test deque inherits from DoublyLinkedList."""
    from deque import Deque
    from doubly_linked_list import DoublyLinkedList
    d = Deque()
    assert isinstance(d._doubly_linked_list, DoublyLinkedList)


def test_appendleft_adds_a_value(deque_fixture):
    """Test the appendleft method adds value."""
    deque_fixture.appendleft(2)
    assert deque_fixture._doubly_linked_list.tail.data == 2


def test_append_and_appendleft_add_multiple_values(deque_fixture):
    """Test the append method adds value."""
    deque_fixture.appendleft(2)
    deque_fixture.append(3)
    assert deque_fixture._doubly_linked_list.tail.data == 3


# def test_dedeque_removes_first_node_added(deque_fixture):
#     """Test that node dedequed is first node added."""
#     deque_fixture.append(2)
#     remove = deque_fixture.popleft()
#     assert remove == 2


# def test_popleft_removes_first_node_added_even_with_multiple_nodes(deque_fixture):
#     """Test that node popleftd is first node added even with multiple nodes."""
#     deque_fixture.append(2)
#     deque_fixture.append(3)
#     remove = deque_fixture.popleft()
#     assert remove == 2