"""Test the functions of priorityq module."""

import pytest


def test_pop_removes_highest_priority():
    """Test pop method removed first value in highest priority."""
    from priorityq import PriorityQueue
    p = PriorityQueue()
    for i in range(3):
        p.insert(i)
    p.insert(8, 2)
    p.insert(10, 2)
    assert p.pop() == 8


def test_pop_removes_raises_error_after_popping_all_values():
    """Test pop method removed first value in highest priority."""
    from priorityq import PriorityQueue
    p = PriorityQueue()
    p.insert(8, 2)
    p.insert(10, 2)
    p.pop()
    p.pop()
    with pytest.raises(IndexError):
        p.pop()


def test_pop_on_new_instance_raises_error():
    """Test pop method on new priority queue raises error."""
    from priorityq import PriorityQueue
    p = PriorityQueue()
    with pytest.raises(IndexError):
        p.pop()


def test_pop_on_emptied_queue_raises_error():
    """Test pop method on empties priority queue raises error."""
    from priorityq import PriorityQueue
    p = PriorityQueue()
    p.insert(2)
    p.pop()
    with pytest.raises(IndexError):
        p.pop()


def test_peek_shows_highest_priority():
    """Test the peek method to show highest priority value."""
    from priorityq import PriorityQueue
    p = PriorityQueue()
    for i in range(3):
        p.insert(i)
    p.insert(8, 2)
    p.insert(10, 2)
    p.insert(0, 33)
    assert p.peek() == 0


def test_peek_on_empty_priority_queue_returns_none():
    """Test the peek method returns none if no values available."""
    from priorityq import PriorityQueue
    p = PriorityQueue()
    assert p.peek() is None
