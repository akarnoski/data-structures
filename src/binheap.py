"""Build a binary min heap object."""
from math import floor


class BinaryHeap(object):
    """Create a Binary Heap object as a Min Heap."""

    def __init__(self):
        """Initialize the heap list to be used by Binary Heap."""
        self._heap_list = []

    def push(self, val):
        """Add new value to heap list and run check heap method."""
        self._heap_list.append(val)
        if len(self._heap_list) == 2:
            self._small_heap()
        self._check_heap()

    def _small_heap(self):
        heap = self._heap_list
        if heap[0] > heap[1]:
            heap[0], heap[1] = heap[1], heap[0]
        return heap

    def _check_heap(self):
        """Check all the children are less than their parents."""
        heap = self._heap_list
        index = floor((len(heap) - 1) / 2)
        i = 0
        while i < index:
            l = (2 * i) + 1
            if heap[i] > heap[l]:
                heap[i], heap[l] = heap[l], heap[i]
            try:
                r = (2 * i) + 2
                if heap[i] > heap[r]:
                    heap[i], heap[r] = heap[r], heap[i]
            except IndexError:  # pragma: no cover
                pass
            i += 1
        return heap

    def pop(self):
        """Remove top value of heap and run check heap method."""
        try:
            heap = self._heap_list
            index = len(heap) - 1
            heap[0], heap[index] = heap[index], heap[0]
            self._heap_list.pop()
            if len(self._heap_list) == 2:
                self._small_heap()
            self._check_heap()
            return heap
        except IndexError:
            raise IndexError('Nothing available to pop')

    def _display(self):  # pragma: no cover
        """Make it easier during testing."""
        for item in self._heap_list:
>>>>>>> 357b1398a2817910fe3b0996d498b7fd975c6976
            print(item)
