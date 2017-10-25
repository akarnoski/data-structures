import pytest


def test_node_has_attributes():
    """Test that the node has attributes."""
    from doubly_linked_list import Node
    n = Node(1, None)
    assert n.data
    assert n.next_node is None
    assert n.previous_node is None
