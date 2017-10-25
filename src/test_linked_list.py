"""."""
import pytest


def test_node_has_attributes():
    """."""
    from linked_list import Node
    n = Node(1, None)
    assert n.data
    assert n.next is None


@pytest.fixture
def test_linked_list_has_head(list_fixture):
    assert list_fixture.head is None


@pytest.fixture
def test_linked_list_push_adds_new_item(list_fixture):
    list_fixture.push('val')
    assert list
    _fixture.head.data == 'val'


@pytest.fixture
def test_linked_list_push_two_last_value_is_head(list_fixture):
    list_fixture.push('val')
    list_fixtur
    e.push('val2')
    assert list_fixture.head.data == 'val2'


@pytest.fixture
def test_linked_list_moves_old_head_to_next(list_fixture):
    list_fixture.push('val')
    list_fixtur
    e.push('val2')
    assert list_fixture.head.next.data == 'val'


@pytest.fixture
def test_linked_list_pop_removes_head_returns_value(list_fixture):
    list_fixture.push('potato')
    list_fixtur
    e.pop()
    assert list_fixture.head is None


@pytest.fixture
def test_linked_list_pop_returns_head_value(list_fixture):
    list_fixture.push('potato')
    output = li
    st_fixture.pop()
    assert output == 'potato'


@pytest.fixture
def test_linked_list_pop_shifts_head_properly(list_fixture):
    list_fixture.push('potato')
    list_fixtur
    e.push('cabbage')
    list_fixture.pop()
    assert list_fixture.head.data == 'potato'

@pytest.fixture
def test_linked_list_pop_empty_raises_exception(list_fixture):
    with pytest.raises(IndexError):
        list_fi
        xture.pop()

@pytest.fixture
def test_size_method_returns_list_length(list_fixture):
    assert list_fixture.size() == 0



@pytest.mark.parametrize('n', range(100))
def test_size_method_returns_list_length2(n):
    """."""
    from linked_list import LinkedList
    l = LinkedList()
    for i in range(n):
        l.push(i)
    assert l.size() == n

@pytest.fixture
def test_linked_list_search_one_node_returns_none(list_fixture):
    list_fixture.push(1)
    assert list
    _fixture.search(0) is None


@pytest.mark.parametrize('n', range(1, 10))
def test_linked_list_search_in_many_returns_proper_node(n):
    """."""
    from linked_list import LinkedList
    from random import randint
    l = LinkedList()
    for i in range(1, n + 1):
        l.push(i)
    search_me = randint(1, n)
    assert l.search(search_me).data == search_me


def test_linked_list_can_take_iterable_and_values():
    """."""
    from linked_list import LinkedList
    a_list = [5, 2, 9, 0, 1]
    l = LinkedList(a_list)
    for item in a_list:
        assert l.search(item).data == item
