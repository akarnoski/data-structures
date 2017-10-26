"""Test functions for stack module."""
import pytest


def test_stack_is_instance_of_stack_object():
    """Test stack is instance of Stack()."""
    from stack import Stack
    s = Stack()
    assert isinstance(s, Stack)


def test_stack_is_instance_of_linked_list():
    """Test stack inherits from LinkedList."""
    from stack import Stack
    from linked_list import LinkedList
    s = Stack()
    assert isinstance(s.linked_list, LinkedList)


def test_stack_pop_removes_top_value_and_returns():
    """Test pop removes item."""
    from stack import Stack
    s = Stack()
    s.push('potato')
    assert s.pop() == 'potato'


def test_stack_pop_shifts_top_properly():
    """Test pop removes last value added."""
    from stack import Stack
    s = Stack()
    s.push('potato')
    s.push('cabbage')
    assert s.pop() == 'cabbage'


@pytest.mark.parametrize('n', range(100))
def test_size_method_returns_list_length(n):
    """Test stack length is appropriate length."""
    from stack import Stack
    s = Stack()
    for i in range(n):
        s.push(i)
    assert len(s) == n
