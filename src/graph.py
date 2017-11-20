"""Create a Graph class data structure."""
from stack import Stack


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
            self._nodes.setdefault(arg, {})

    def add_edge(self, val1, val2, weight):
        """Add a new edge to the Graph and connects the values.

        If either value doesn't exist they will be created.
        """
        self.add_node(val1, val2)
        if val2 in self._nodes[val1]:  # pragma: no cover
            pass
        else:
            self._nodes[val1].update({val2: weight})

    def del_node(self, val):
        """Delete the node containing the given value."""
        try:
            if val in self._nodes:
                del self._nodes[val]
            for key in self._nodes:
                if val in list(self._nodes[key]):
                    self._nodes[key].pop(val)
        except KeyError:
            raise KeyError("No such Node exists")

    def del_edge(self, val1, val2):
        """Delete the edge connecting the two values."""
        try:
            for node in self._nodes[val1]:
                if val2 == node:
                    self._nodes[val1].pop(node)
                    return
            raise IndexError("No connection between those two Nodes.")
        except KeyError:
            raise KeyError("No Node with given first value.")

    def has_node(self, val):
        """Return True is node containing value exists in Graph."""
        return True if val in self._nodes else False

    def neighbors(self, val):
        """Return list of all nodes connected to node containing the value."""
        return list(self._nodes[val].keys())

    def adjacent(self, val1, val2):
        """Return True if there is an edge connecting the two values."""
        return val2 in self._nodes[val1]

    def depth_first_traversal(self, start):
        """Perform a depth-first traversal and return full visited path."""
        if start not in self._nodes:
            raise KeyError("No such value")
        path = []
        visit = Stack()
        curr = start
        while True:
            try:
                neighbors = self.neighbors(curr)
                for n in neighbors:
                    visit.push(n)
                path.append(curr)
                curr = visit.pop()
            except IndexError:
                break
        return path

    def breadth_first_traversal(self, start):
        """Perform a breadth-first traversal and return full visited path."""
        if start not in self._nodes:
            raise KeyError("No such value")
        path, visit = [], []
        curr = start
        while True:
            try:
                path.append(curr)
                visit.extend(self.neighbors(curr))
                curr = visit[0]
                visit = visit[1:]
            except IndexError:
                break
        return path

    def shortest_path(self, start, end, graph=None,
                      visited=[], dist={}, predecessors={}):
        """Method to find the shortest path between two given values."""
        graph = self._nodes
        if start not in graph:
            raise TypeError("The start value can't be found.")
        if end not in graph:
            raise TypeError("The end value can't be found.")
        if start == end:
            path = []
            pred = end
            while pred is not None:
                path.append(pred)
                pred = predecessors.get(pred, None)
            print('shortest path: ' + str(path))
        else:
            if not visited:
                dist[start] = 0
            for neighbor in graph[start]:
                if neighbor not in visited:
                    new_distance = dist[start] + graph[start][neighbor]
                    if new_distance < dist.get(neighbor, float('inf')):
                        dist[neighbor] = new_distance
                        predecessors[neighbor] = start
            visited.append(start)
            unvisited = {}
            for k in graph:
                if k not in visited:
                    unvisited[k] = dist.get(k, float('inf'))
            x = min(unvisited, key=unvisited.get)
            self.shortest_path(x, end, graph, visited, dist, predecessors)
