"""Function for the radix sort alogorithm."""
from que_ import Queue


def radix_sort(input):
    """Radix sort function."""
    if not isinstance(input, list):
        raise TypeError('Please insert a list')
    if len(input) <= 1:
        return input
    index, output = _preppin_nums(input)
    buckets = _makin_buckets()
    place = 1
    # while index != 0:     
    for number in output:
        print(index)
        digit = number[-place]
        # bucket = buckets[digit]
    #     bucket.enqueue(number)
    # test = buckets[1].dequeue()
    print(digit)


def _preppin_nums(input):
    """Function to getting input ready for sorting."""
    max_size = 0
    output = []
    for item in input:
        breakdown = [int(d) for d in str(item)]
        output.append(breakdown)
        if len(breakdown) > max_size:
            max_size = len(breakdown)
    return [max_size - 1, output]


def _makin_buckets():
    """Make some buckets for some nums to put sorted stuff in."""
    buckets = []
    for i in range(10):
        q = Queue()
        buckets.append(q)
    return buckets
