"""Function for the radix sort alogorithm."""
from que_ import Queue


def radix_sort(in_list):
    """Radix sort function."""
    if not isinstance(in_list, list):
        raise TypeError('Please insert a list')
    if len(in_list) <= 1:
        return in_list
    max_index, output = _preppin_nums(in_list)
    buckets = _makin_buckets()
    place = 1
    while place != max_index:
        for number in output:
            digit = number[-place]
            bucket = buckets[digit]
            bucket.enqueue(number)
        place += 1
    shit = []
    for i in range(10):
        while buckets[i].size() != 0:
            shit.append(buckets[i].dequeue())
    return shit


def _preppin_nums(in_list):
    """Function to getting in_list ready for sorting."""
    max_size = 0
    output = []
    for item in in_list:
        breakdown = [int(d) for d in str(item)]
        output.append(breakdown)
        if len(breakdown) > max_size:
            max_size = len(breakdown)
    return [max_size, output]


def _makin_buckets():
    """Make some buckets for some nums to put sorted stuff in."""
    buckets = []
    for i in range(10):
        q = Queue()
        buckets.append(q)
    return buckets
