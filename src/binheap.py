"""."""


class BinaryHeap(object):
    """Create a Doubly Linked List."""

    def __init__(self):
        """."""
        self.heap_list = []

    def push(self, val):
        """."""
        self.heap_list.append(val)

    def check_heap(self):
        """."""
        heap = self.heap_list
        index = (len(heap) - 1) / 2
        i = 0
        while i <= index:
            l = (2 * i) + 1
            r = (2 * i) + 2
            if heap[i] > heap[l]:
                print(i)
                heap[i], heap[l] = heap[l], heap[i]
            try:
                if heap[i] > heap[r]:
                    heap[i], heap[r] = heap[r], heap[i]
            except IndexError:
                pass
            i += 1

    def display(self):
        for item in self.heap_list:
            print(item)
