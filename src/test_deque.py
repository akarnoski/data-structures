"""Test functions for deque module."""
import pytest


def test_deque_is_instance_of_deque_object():
    """Test deque is instance of Deque()."""
    from deque import Deque
    d = Deque()
    assert isinstance(d, Deque)


def test_deque_is_instance_of_doubly_linked_list():
    """Test deque inherits from DoublyLinkedList."""
    from deque import Deque
    from doubly_linked_list import DoublyLinkedList
    d = Deque()
    assert isinstance(d._doubly_linked_list, DoublyLinkedList)


def test_append_adds_a_value(deque_fixture):
    """Test the append method adds value."""
    deque_fixture.append(2)
    assert deque_fixture._doubly_linked_list.tail.data == 2


def test_append_adds_multiple_values_and_checks_back(deque_fixture):
    """Test the append method adds value."""
    deque_fixture.append(2)
    deque_fixture.append(3)
    assert deque_fixture._doubly_linked_list.tail.data == 3


def test_dedeque_removes_first_node_added(deque_fixture):
    """Test that node dedequed is first node added."""
    deque_fixture.append(2)
    remove = deque_fixture.popleft()
    assert remove == 2


def test_popleft_removes_first_node_added_even_with_multiple_nodes(deque_fixture):
    """Test that node popleft'd is first node added even with multiple nodes."""
    deque_fixture.append(2)
    deque_fixture.append(3)
    remove = deque_fixture.popleft()
    assert remove == 2


def test_popleft_raises_exception_on_empty_deque(deque_fixture):
    """Test that index error is raised when dequeuing empty deque."""
    with pytest.raises(IndexError):
        deque_fixture.popleft()


def test_peek_returns_next_value_to_be_dedequed(deque_fixture):
    """Test that value returned is from node next to be dedequed."""
    deque_fixture.append(2)
    assert deque_fixture.peek() == 2


def test_peek_returns_none_on_empty_deque(deque_fixture):
    """Test that None is returned on empty list peek."""
    assert deque_fixture.peek() is None


def test_size_method_returns_list_length_0_if_empty(deque_fixture):
    """Test size method returns 0 on empty deque."""
    assert deque_fixture.size() == 0


def test_size_method_returns_list_length(deque_fixture):
    """Test size method on deque."""
    deque_fixture.append(2)
    deque_fixture.append(3)
    assert deque_fixture.size() == 2


def test_len_function_works_with_deque(deque_fixture):
    """Test that deque works with len function."""
    assert len(deque_fixture) == 0


def test_deque_append_left_adds_node_to_front_of_deque(deque_fixture):
    """Test that append adds node at the front."""
    deque_fixture.appendleft(1)
    assert deque_fixture._doubly_linked_list.head.data == 1
    assert deque_fixture._doubly_linked_list.tail.data == 1


def test_deque_append_left_adds_multiple_nodes_to_front_of_deque(deque_fixture):
    """Test that append adds node at the front."""
    deque_fixture.appendleft(1)
    deque_fixture.appendleft(2)
    deque_fixture.appendleft(3)
    deque_fixture.appendleft(4)
    assert deque_fixture._doubly_linked_list.head.data == 4


def test_deque_pop_removes_node_at_end_of_deque(deque_fixture):
    """Test that pop removes the tail node."""
    deque_fixture.append(2)
    deque_fixture.append(3)
    assert deque_fixture.pop() == 3


def test_deque_pop_raises_index_error_on_empty_deque(deque_fixture):
    """Test that pop raises IndexError on an empty deque."""
    with pytest.raises(IndexError):
        deque_fixture.pop()


def test_deque_peek_left_shows_value_of_node_at_head(deque_fixture):
    """Test that peekleft shows next node value that would be removed by popleft."""
    deque_fixture.append(2)
    deque_fixture.appendleft(5)
    assert deque_fixture.peekleft() == 5


def test_deque_peek_left_raises_error_on_empty_list(deque_fixture):
    """Test that peekleft returns None on an empty list."""
    assert deque_fixture.peekleft() is None
