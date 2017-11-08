"""Test functions for linked_list module."""
import pytest


@pytest.fixture
def list_fixture():
    """A fixture for the Linked List."""
    from linked_list import LinkedList
    l = LinkedList()
    return l


def test_node_has_attributes():
    """Test that the node has attributes."""
    from linked_list import Node
    n = Node(1, None)
    assert n.data
    assert n.next is None


def test_linked_list_has_head(list_fixture):
    """Test if the linked list has head node."""
    assert list_fixture.head is None


def test_linked_list_push_adds_new_item(list_fixture):
    """Test that if new node is added."""
    list_fixture.push('val')
    assert list_fixture.head.data == 'val'


def test_linked_list_push_two_last_value_is_head(list_fixture):
    """Test that two nodes are added."""
    list_fixture.push('val')
    list_fixture.push('val2')
    assert list_fixture.head.data == 'val2'


def test_linked_list_moves_old_head_to_next(list_fixture):
    """Test that the new node is moved to head."""
    list_fixture.push('val')
    list_fixture.push('val2')
    assert list_fixture.head.next.data == 'val'


def test_linked_list_pop_removes_head_returns_value(list_fixture):
    """Test pop removes head."""
    list_fixture.push('potato')
    list_fixture.pop()
    assert list_fixture.head is None


def test_linked_list_pop_returns_head_value(list_fixture):
    """Test pop returns value."""
    list_fixture.push('potato')
    output = list_fixture.pop()
    assert output == 'potato'


def test_linked_list_pop_shifts_head_properly(list_fixture):
    """Test pop shifts head."""
    list_fixture.push('potato')
    list_fixture.push('cabbage')
    list_fixture.pop()
    assert list_fixture.head.data == 'potato'


def test_linked_list_pop_empty_raises_exception(list_fixture):
    """Test pop on empty linked list raises exception."""
    with pytest.raises(IndexError):
        list_fixture.pop()


def test_size_method_returns_list_length(list_fixture):
    """Test size method on linked list."""
    assert list_fixture.size() == 0


@pytest.mark.parametrize('n', range(100))
def test_size_method_returns_list_length2(n, list_fixture):
    """Test size method on linked list."""
    for i in range(n):
        list_fixture.push(i)
    assert list_fixture.size() == n


def test_linked_list_search_one_node_returns_none(list_fixture):
    """Test search returns none."""
    list_fixture.push(1)
    assert list_fixture.search(0) is None


@pytest.mark.parametrize('n', range(1, 10))
def test_linked_list_search_in_many_returns_proper_node(n, list_fixture):
    """Test search returns correct node."""
    from random import randint
    for i in range(1, n + 1):
        list_fixture.push(i)
    search_me = randint(1, n)
    assert list_fixture.search(search_me).data == search_me


def test_linked_list_can_take_iterable_and_values():
    """Test linked list can take iterables and values."""
    from linked_list import LinkedList
    a_list = [5, 2, 9, 0, 1]
    l = LinkedList(a_list)
    for item in a_list:
        assert l.search(item).data == item


def test_linked_list_removes_a_single_node(list_fixture):
    """Test that remove works with only one node."""
    list_fixture.push(1)
    list_fixture.remove(1)
    assert list_fixture.head is None


def test_linked_list_remove_raises_index_error_on_empty_list(list_fixture):
    """Test that remove raises error on empty list."""
    with pytest.raises(IndexError):
        list_fixture.remove(1)


def test_linked_list_remove_works(list_fixture):
    """Test that remove reassigns node nexts."""
    list_fixture.push(2)
    list_fixture.push(3)
    list_fixture.push(4)
    list_fixture.remove(3)
    assert list_fixture.head.next.data == 2


def test_linked_list_remove_raises_attr_error(list_fixture):
    """Test that remove function raises attr error."""
    list_fixture.push(2)
    list_fixture.push(3)
    list_fixture.push(4)
    with pytest.raises(ValueError):
        list_fixture.remove(5)


def test_linked_list_display_returns_correctly(list_fixture):
    """Test that display displays correctly."""
    list_fixture.push(2)
    list_fixture.push(3)
    list_fixture.push(4)
    assert list_fixture.display() == "(4, 3, 2)"
