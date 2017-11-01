"""Test functions for deque module."""
import pytest


def test_binheap_is_instance_of_BinHeap_object():
    """Test binheap is instance of BinaryHeap()."""
    from binheap import BinaryHeap
    b = BinaryHeap()
    assert isinstance(b, BinaryHeap)


def test_binheap_inits_with_empty_list(bh_fixture):
    """Test binheap is initialized with empty list."""
    assert bh_fixture._heap_list == []


def test_binheap_push_returns_list_with_one_value(bh_fixture):
    """Test binheap is initialized with empty list."""
    bh_fixture.push(3)
    assert len(bh_fixture._heap_list) == 1
