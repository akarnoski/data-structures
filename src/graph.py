"""Create a Graph class data structure."""


class Graph(object):
    """Graph object."""

    def __init__(self):
        """Graph things on initialization."""
        self._nodes = {}

    def nodes(self):
        """List all nodes in the Graph."""
        return [key for key in self._nodes]

    def edges(self):
        """List all edges in the Graph."""
        return self._nodes

    def add_node(self, *args):
        """Add a new node to the Graph."""
        for arg in args:
            self._nodes.setdefault(arg, [])

    def add_edge(self, val1, val2):
        """Add a new edge to the Graph and connects the values.

        If either value doesn't exist they will be created.
        """
        self.add_node(val1, val2)
        if val2 in self._nodes[val1]:  # pragma: no cover
            pass
        else:
            self._nodes[val1].append(val2)

    def del_node(self, val):
        """Delete the node containing the given value."""
        try:
            del self._nodes[val]
            for key in self._nodes:
                if val in self._nodes[key]:
                    self._nodes[key].remove(val)
        except KeyError:
            raise KeyError("No such Node exists")

    def del_edge(self, val1, val2):
        """Delete the edge connecting the two values."""
        try:
            for node in self._nodes[val1]:
                if val2 == node:
                    self._nodes[val1].remove(node)
                    return
            raise IndexError("No connection between those two Nodes.")
        except KeyError:
            raise KeyError("No Node with given first value.")

    def has_node(self, val):
        """Return True is node containing value exists in Graph."""
        return True if val in self._nodes else False

    def neighbors(self, val):
        """Return list of all nodes connected to the node containing the value."""
        return self._nodes[val]

    def adjacent(self, val1, val2):
        """Return True if there is an edge connecting the two values."""
        return val2 in self._nodes[val1]
