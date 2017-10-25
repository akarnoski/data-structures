import pytest


def test_stack_has_values():
    from stack import Stack
    s = Stack()
    assert isinstance(s, Stack)


def test_stack_is_instance_of_linked_list():
    from stack import Stack
    from linked_list import LinkedList
    s = Stack()
    assert isinstance(s.linked_list, LinkedList)


def test_stack_pop_removes_top_value_and_returns():
    from stack import Stack
    s = Stack()
    s.push('potato')
    assert s.pop() == 'potato'


def test_stack_pop_shifts_top_properly():
    from stack import Stack
    s = Stack()
    s.push('potato')
    s.push('cabbage')
    assert s.pop() == 'cabbage'


@pytest.mark.parametrize('n', range(100))
def test_size_method_returns_list_length(n):
    from stack import Stack
    s = Stack()
    for i in range(n):
        s.push(i)
    assert len(s) == n


