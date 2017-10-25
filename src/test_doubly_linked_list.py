import pytest


def test_node_has_attributes():
    """test that the node has attributes."""
    from doubly_linked_list import Node
    n = Node(1, None)
    assert n.data
    assert n.next is None
    assert n.previous is None
