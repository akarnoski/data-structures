"""Test functions for the graph module."""
import pytest


def test_graph_inits_with_empty_nodes_dict(graph_fixture):
    """Test that Graph initializes with empty nodes dict."""
    assert graph_fixture._nodes == {}


def test_add_node_adds_to_nodes_list(graph_fixture):
    """Test that adding a node attaches it to the Graph's node list."""
    graph_fixture.add_node(1)
    assert len(graph_fixture._nodes) == 1
    assert graph_fixture._nodes[1] == []


def test_del_node_removes_node_with_given_value(graph_fixture):
    """Test that removing the node with the given value works."""
    for i in range(5):
        graph_fixture.add_node(i)
    assert len(graph_fixture._nodes) == 5
    graph_fixture.del_node(3)
    assert len(graph_fixture._nodes) == 4


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


def test_del_node_raises_key_error_on_empty_graph(graph_fixture):
        """Test del_node raises KeyError if no Nodes in Graph."""
        with pytest.raises(KeyError):
            graph_fixture.del_node(2)


def test_del_node_raises_key_error_on_a_list(graph_fixture):
    """Test del_node raises KeyError.

    Will raise the error if looking for a Node with the given value and it
    is not in the Graph.
    """
    for i in range(3):
        graph_fixture.add_node(i)
    with pytest.raises(KeyError):
        graph_fixture.del_node(8)


def test_adjacent_returns_false(graph_fixture):
    """Return false if value of second Node is not connected to first Node."""
    graph_fixture.add_edge(1, 2)
    assert graph_fixture.adjacent(1, 3) is False


def test_adjacent_returns_true(graph_fixture):
    """Return true if value of second Node is connected to first Node."""
    graph_fixture.add_edge(1, 2)
    assert graph_fixture.adjacent(1, 2) is True


def test_del_edge_raises_error(graph_fixture):
    """Test del_edge raises IndexError.

    Will raise the error if trying to remove an edge between Nodes that doesn't
    exit.
    """
    graph_fixture.add_edge(1, 2)
    with pytest.raises(IndexError):
        graph_fixture.del_edge(1, 3)


def test_neighbors_returns_all_connected_nodes(graph_fixture):
    """Test neighbors will return all the Nodes connected to Node containing the given value."""
    graph_fixture.add_edge(1, 2)
    assert len(graph_fixture.neighbors(1)) == 1
    graph_fixture.add_edge(1, 3)
    assert len(graph_fixture.neighbors(1)) == 2


def test_nodes_returns_list_of_nodes(graph_fixture):
    """Test that nodes will return a list of all the created Nodes."""
    for i in range(4):
        graph_fixture.add_node(i)
    assert len(graph_fixture.nodes()) == 4


def test_edges_returns_all_edges(graph_fixture):
    """Test that edges will return a dict of all edges."""
    graph_fixture.add_edge(1, 2)
    graph_fixture.add_edge(2, 3)
    graph_fixture.add_edge(3, 7)
    assert graph_fixture.edges() == {1: [2], 2: [3], 3: [7], 7: []}


def test_del_node_removes_all_memory_of_node(graph_fixture):
    """Test that the deletion of the Node goes all the way down the family."""
    graph_fixture.add_edge(1, 2)
    graph_fixture.add_edge(2, 1)
    graph_fixture.del_node(1)
    assert graph_fixture.nodes() == [2]
    assert graph_fixture.edges() == {2: []}


def test_del_edge_works(graph_fixture):
    """Test that del_edge will actually delete the edge."""
    graph_fixture.add_edge(1, 2)
    graph_fixture.add_edge(1, 3)
    graph_fixture.del_edge(1, 2)
    assert graph_fixture.edges() == {1: [3], 2: [], 3: []}


def test_del_edge_raises_key_error(graph_fixture):
    """Test that del_edge raises KeyError.

    Error will be raised if the first given value is not in the Graph.
    """
    with pytest.raises(KeyError):
        graph_fixture.del_edge(1, 2)


def test_depth_first_traversal(graph_fixture):
    """Test the functionality of the depth first traversal."""
    DEPTH_LIST = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("B", "E"),
        ("C", "G"),
        ("C", "F"),
    ]
    for test in DEPTH_LIST:
        graph_fixture.add_edge(test[0], test[1])
    check_graph = graph_fixture.depth_first_traversal("A")
    returned_list = ['A', 'C', 'F', 'G', 'B', 'E', 'D']
    assert check_graph == returned_list


def test_depth_first_traversal_raises_error(graph_fixture):
    """Test the functionality of the depth first traversal."""
    DEPTH_LIST = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("B", "E"),
        ("C", "G"),
        ("C", "F"),
    ]
    for test in DEPTH_LIST:
        graph_fixture.add_edge(test[0], test[1])
    with pytest.raises(KeyError):
        graph_fixture.depth_first_traversal("M")


def test_empty_graph_depth_first_traversal_raises_error(graph_fixture):
    """Test the functionality of the depth first traversal."""
    with pytest.raises(KeyError):
        graph_fixture.depth_first_traversal("M")


def test_breadth_first_traversal(graph_fixture):
    """Test the functionality of the breadth first traversal."""
    DEPTH_LIST = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("B", "E"),
        ("C", "G"),
        ("C", "F"),
    ]
    for test in DEPTH_LIST:
        graph_fixture.add_edge(test[0], test[1])
    check_graph = graph_fixture.breadth_first_traversal("A")
    returned_list = ['A', 'B', 'C', 'D', 'E', 'G', 'F']
    assert check_graph == returned_list


def test_breadth_first_traversal_raises_error(graph_fixture):
    """Test the functionality of the breadth first traversal."""
    DEPTH_LIST = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("B", "E"),
        ("C", "G"),
        ("C", "F"),
    ]
    for test in DEPTH_LIST:
        graph_fixture.add_edge(test[0], test[1])
    with pytest.raises(KeyError):
        graph_fixture.breadth_first_traversal("M")


def test_empty_graph_depth_first_traversal_raises_error(graph_fixture):
    """Test the functionality of the breadth first traversal."""
    with pytest.raises(KeyError):
        graph_fixture.breadth_first_traversal("M")
