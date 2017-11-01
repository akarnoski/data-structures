"""Test functions for priorityq module."""


def test_pop_works_correctly():
    """."""
    from priorityq import PriorityQueue
    p = PriorityQueue()
    for i in range(3):
        p.insert(i)
    p.insert(8, 2)
    p.insert(10, 2)
    assert p.pop() == 8


def test_peek_works_correctly():
    """."""
    from priorityq import PriorityQueue
    p = PriorityQueue()
    for i in range(3):
        p.insert(i)
    p.insert(8, 2)
    p.insert(10, 2)
    p.insert(0, 33)
    assert p.peek() == 0
