"""Test functions for the graph module."""
import pytest


def test_node_object_inits_with_no_val():
    """Test that Node object initializes without a value."""
    from graph import Node
    n = Node()
    assert n.value is None


def test_graph_inits_with_empty_nodes_list(graph_fixture):
    """Test that Graph initializes with empty nodes list."""
    assert graph_fixture._nodes_list == []


def test_add_node_adds_to_nodes_list(graph_fixture):
    """Test that adding a node attaches it to the Graph's node list."""
    graph_fixture.add_node(1)
    assert len(graph_fixture._nodes_list) == 1
    assert graph_fixture._nodes_list[0].value == 1


def test_del_node_removes_node_with_given_value(graph_fixture):
    """Test that removing the node with the given value works."""
    for i in range(5):
        graph_fixture.add_node(i)
    assert len(graph_fixture._nodes_list) == 5
    graph_fixture.del_node(3)
    assert len(graph_fixture._nodes_list) == 4


def test_has_node_returns_true_if_node_in_graph(graph_fixture):
    """Test that has_node returns True if in fact the Node is in the Graph."""
    for i in range(5):
        graph_fixture.add_node(i)
    assert graph_fixture.has_node(3) is True


def test_has_node_returns_false_if_node_not_in_graph(graph_fixture):
    """Test that has_node returns False if Node is not in Graph."""
    for i in range(5):
        graph_fixture.add_node(i)
    assert graph_fixture.has_node(7) is False


def test_add_node_raises_value_error(graph_fixture):
    """Test add_node raises ValueError.

    Will raise the error if attempting to add a Node with a value that
    is already in the Graph.
    """
    graph_fixture.add_node(2)
    with pytest.raises(ValueError):
        graph_fixture.add_node(2)


def test_del_node_raises_index_error_on_empty_graph(graph_fixture):
        """Test del_node raises IndexError if no Nodes in Graph."""
        with pytest.raises(IndexError):
            graph_fixture.del_node(2)


def test_del_node_raises_index_error_on_a_list(graph_fixture):
    """Test del_node raises IndexError.

    Will raise the error if looking for a Node with the given value and it
    is not in the Graph.
    """
    for i in range(3):
        graph_fixture.add_node(i)
    with pytest.raises(IndexError):
        graph_fixture.del_node(8)


def test_adjacent_returns_false(graph_fixture):
    """Return false if value of second Node is not connected to first Node."""
    graph_fixture.add_edge(1, 2)
    assert graph_fixture.adjacent(1, 3) is False


def test_adjacent_returns_true(graph_fixture):
    """Return true if value of second Node is connected to first Node."""
    graph_fixture.add_edge(1, 2)
    assert graph_fixture.adjacent(1, 2) is True


def test_del_edge_removes_connection(graph_fixture):
    """Test del_edge removes the connection between two Nodes."""
    graph_fixture.add_edge(1, 2)
    graph_fixture.add_edge(1, 3)
    graph_fixture.del_edge(1, 3)
    assert len(graph_fixture.edges()[1]) == 1
