"""Build a binary heap object."""


class BinaryHeap(object):
    """Create a Binary Heap object."""

    def __init__(self):
        """Initialize."""
        self.heap_list = []

    def push(self, val):
        """Add new value."""
        self.heap_list.append(val)

    def _check_heap(self):
        from math import floor
        """Check all the children are less than their parents."""
        heap = self.heap_list
        index = floor((len(heap) - 1) / 2)
        i = 0
        while i < index:
            l = (2 * i) + 1
            if heap[i] > heap[l]:
                print(i)
                heap[i], heap[l] = heap[l], heap[i]
            try:
                r = (2 * i) + 2
                if heap[i] > heap[r]:
                    heap[i], heap[r] = heap[r], heap[i]
            except IndexError:
                pass
            i += 1
        return heap

    def _display(self):
        """Make it easier during testing."""
        for item in self.heap_list:
            print(item)
