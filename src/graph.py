"""Create a Graph class data structure."""


class Node(object):
    """Node object to put into the Graph."""

    def __init__(self, value=None):
        """Node things on initialization."""
        self.value = value

    def __repr__(self):
        """Make Node objects do repr things."""
        return str(self.value)


class Graph(object):
    """Graph object."""

    def __init__(self):
        """Graph things on initialization."""
        self._nodes_list = []
        self._check_list = []
        self._edge_list = {}

    def nodes(self):
        """List all nodes in the Graph."""
        return self._nodes_list

    def edges(self):
        """List all edges in the Graph."""
        return self._edge_list

    def add_node(self, val):
        """Add a new node to the Graph."""
        if val in self._check_list:
            raise ValueError("Value already in Graph.")
        new_node = Node(val)
        self._nodes_list.append(new_node)
        self._check_list.append(val)
        return new_node

    def add_edge(self, val1, val2):
        """Add a new edge to the Graph and connects the values.

        If either value doesn't exist they will be created.
        """
        try:
            node1 = self.add_node(val1)
        except ValueError:
            for node in self._nodes_list:
                if val1 == node.value:
                    node1 = node

        try:
            node2 = self.add_node(val2)
        except ValueError:
            for node in self._nodes_list:
                if val2 == node.value:
                    node2 = node
        try:
            edge_list = self._edge_list[val1]
            for node in edge_list:
                if val2 == node.value:
                    edge_list.remove(node)
        except KeyError:
            pass
        self._edge_list.setdefault(node1.value, []).append(node2)

    def del_node(self, val):
        """Delete the node containing the given value."""
        if self._nodes_list == []:
            raise IndexError("No Nodes in Graph.")
        for node in self._nodes_list:
            if node.value == val:
                return self._nodes_list.remove(node)
        raise IndexError("No such Node in Graph.")

    def del_edge(self, val1, val2):
        """Delete the edge connecting the two values."""
        try:
            edge_list = self._edge_list[val1]
            for node in edge_list:
                if val2 == node.value:
                    return edge_list.remove(node)
            raise IndexError("No connection between those two Nodes.")
        except KeyError:
            raise KeyError("No Node with given first value.")

    def has_node(self, val):
        """Return True is node containing value exists in Graph."""
        for node in self._nodes_list:
            if node.value == val:
                return True
        return False

    def neighbors(self, val):
        """Return list of all nodes connected to the node containing the value."""
        return self._edge_list[val]

    def adjacent(self, val1, val2):
        """Return True if there is an edge connecting the two values."""
        edge_list = self._edge_list[val1]
        for node in edge_list:
            if val2 == node.value:
                return True
        return False
