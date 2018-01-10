"""Test functions for the doubly_linked_list module."""
import pytest


def test_node_has_attributes():
    """Test that the node has attributes."""
    from doubly_linked_list import Node
    n = Node(1, None)
    assert n.data
    assert n.next_node is None
    assert n.previous_node is None


def test_double_linked_list_has_head(dll_fixture):
    """Test if the linked list has head node."""
    assert dll_fixture.head is None


def test_double_linked_list_push_adds_new_item(dll_fixture):
    """Test that if new node is added."""
    dll_fixture.push('val')
    assert dll_fixture.head.data == 'val'


def test_double_linked_list_push_two_last_value_is_head(dll_fixture):
    """Test that two nodes are added."""
    dll_fixture.push('val')
    dll_fixture.push('val2')
    assert dll_fixture.head.data == 'val2'


def test_double_linked_list_moves_old_head_to_next(dll_fixture):
    """Test that the new node is moved to head."""
    dll_fixture.push('val')
    dll_fixture.push('val2')
    assert dll_fixture.head.next_node.data == 'val'


def test_double_linked_list_pop_removes_head_returns_value(dll_fixture):
    """Test pop removes head."""
    dll_fixture.push('potato')
    dll_fixture.pop()
    assert dll_fixture.head is None


def test_double_linked_list_pop_returns_head_value(dll_fixture):
    """Test pop returns value."""
    dll_fixture.push('potato')
    output = dll_fixture.pop()
    assert output == 'potato'


def test_double_linked_list_pop_shifts_head_properly(dll_fixture):
    """Test pop shifts head."""
    dll_fixture.push('potato')
    dll_fixture.push('cabbage')
    dll_fixture.pop()
    assert dll_fixture.head.data == 'potato'


def test_double_linked_list_pop_empty_raises_exception(dll_fixture):
    """Test pop on empty linked list raises exception."""
    with pytest.raises(IndexError):
        dll_fixture.pop()


def test_size_method_returns_list_length(dll_fixture):
    """Test size method on linked list."""
    assert dll_fixture.size() == 0


@pytest.mark.parametrize('n', range(100))
def test_size_method_returns_list_length2(n):
    """Test size method on linked list."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    for i in range(n):
        dll.push(i)
    assert dll.size() == n


def test_double_linked_list_append_value(dll_fixture):
    """Test double linked list appends value to tail."""
    for i in range(5):
        dll_fixture.push(i)
    dll_fixture.append(6)
    tail = dll_fixture.tail.data
    assert tail == 6


def test_double_linked_list_shift_method():
    """Test double linked list removes last value."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    for i in range(5):
        dll.push(i)
    dll.shift()
    tail = dll.tail.data
    assert tail == 1


def test_shift_will_not_break_if_pop_and_shift_are_used_on_same_list(dll_fixture):
    """Test that shift won't break if it there is nothing in the list."""
    dll_fixture.push(1)
    dll_fixture.push(2)
    dll_fixture.push(3)
    dll_fixture.pop()
    dll_fixture.pop()
    dll_fixture.shift()
    with pytest.raises(IndexError):
        dll_fixture.shift()
