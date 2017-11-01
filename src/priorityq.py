"""Create Priority Q object."""


class PriorityQueue(object):
    """Create a new PriorityQueue object."""

    def __init__(self):
        """Initialized value of a Priority Queue."""
        self._priority_dict = {}

    def insert(self, value, priority=0):
        """Insert a new value with priority zero unless otherwise stated."""
        self._priority_dict.setdefault(priority, []).append(value)

    def pop(self):
        """Pop first highest priority value."""
        highest_priority = max(self._priority_dict, key=int)
        return self._priority_dict[highest_priority].pop(0)

    def peek(self):
        """Show the first highest priority value."""
        highest_priority = max(self._priority_dict, key=int)
        return self._priority_dict[highest_priority][0]
