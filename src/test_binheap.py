"""Test functions for deque module."""
import pytest


def test_binheap_is_instance_of_binheap_object():
    """Test binheap is instance of BinaryHeap()."""
    from binheap import BinaryHeap
    b = BinaryHeap()
    assert isinstance(b, BinaryHeap)


def test_binheap_inits_with_empty_list(bh_fixture):
    """Test binheap is initialized with empty list."""
    assert bh_fixture._heap_list == []


def test_binheap_push_appends_to_list_with_one_value(bh_fixture):
    """Test binheap successfully pushes one value."""
    bh_fixture.push(3)
    assert len(bh_fixture._heap_list) == 1


def test_binheap_push_appends_to_list_with_multiple_values(bh_fixture):
    """Test binheap successfully pushes multiple values."""
    for i in range(5):
        bh_fixture.push(i)
    assert len(bh_fixture._heap_list) == 5


def test_binheap_small_heap_correctly_orders_pushed_values(bh_fixture):
    """Test that binheap correctly orders values when there aren't very many."""
    bh_fixture.push(2)
    bh_fixture.push(5)
    assert bh_fixture._heap_list[0] == 2


def test_binheap_check_heap_correctly_orders_multiple_pushed_values(bh_fixture):
    """Test that binheap orders values correctly."""
    bh_fixture.push(2)
    bh_fixture.push(10)
    bh_fixture.push(8)
    bh_fixture.push(4)
    bh_fixture.push(7)
    assert bh_fixture._heap_list == [2, 4, 8, 10, 7]


def test_binheap_pop_returns_popped_value(bh_fixture):
    """Test correct value gets popped."""
    bh_fixture.push(2)
    bh_fixture.push(10)
    bh_fixture.push(7)
    bh_fixture.pop()
    assert bh_fixture._heap_list == [7, 10]


def test_binheap_pop_raises_index_error_on_empty_heap(bh_fixture):
    """Make sure binheap raises IndexError."""
    with pytest.raises(IndexError):
        bh_fixture.pop()
