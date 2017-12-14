"""Function for the radix sort alogorithm."""
from que_ import Queue


def radix_sort(in_list):
    """Radix sort function."""
    if not isinstance(in_list, list):
        raise TypeError('Please insert a list')
    if len(in_list) <= 1:
        return in_list
    max_index, output = _preppin_nums(in_list)
    buckets = [[] for _ in range(10)]
    start_index = 1
    while start_index <= max_index:
        for number in output:
            try:
                digit = number[-start_index]
                bucket = buckets[digit]
                bucket.append(number)
            except IndexError:
                buckets[0].append(number)
        start_index += 1
        output = [y for x in buckets for y in x]
        buckets = [[] for _ in range(10)]
    out_list = []
    for row in output:
        out_list.append(int(''.join([str(elem) for elem in row])))
    return out_list


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


if __name__ == '__main__':  # pragma: no cover
    import timeit
    good = [123, 456, 234, 543, 876, 23]
    bad = [123, 56, 456234, 543, 876, 23]
    average = [123, 456, 234, 543, 876, 23]
    print('A good time: {}'.format(timeit.timeit("radix_sort(good)", setup="from __main__ import radix_sort, good")))
    print('A bad time: {}'.format(timeit.timeit("radix_sort(bad)", setup="from __main__ import radix_sort, bad")))
    print('An average time: {}'.format(timeit.timeit("radix_sort(average)", setup="from __main__ import radix_sort, average")))