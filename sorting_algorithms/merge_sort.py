"""Create an merge sort algorithm."""


def merge_sort(in_list):
    """Sort a given in_list with merge sort."""
    if not isinstance(in_list, list):
        raise TypeError('Please insert a list')
    if len(in_list) == 1:
        return in_list
    if len(in_list) == 2:
        if in_list[0] > in_list[1]:
            in_list[0], in_list[1] = in_list[1], in_list[0]
        return in_list
    else:
        half = int(len(in_list) / 2)
        one_half = merge_sort(in_list[:half])
        two_half = merge_sort(in_list[half:])
        return _sort(one_half, two_half)


def _sort(one_half, two_half):
    output = []
    while len(one_half) != 0 and len(two_half) != 0:
        if one_half[0] < two_half[0]:
            output.append(one_half.pop(0))
        else:
            output.append(two_half.pop(0))
    if len(one_half) == 0:
        output += two_half
    else:
        output += one_half
    return output


if __name__ == '__main__':  # pragma: no cover
    import timeit
    good = [1, 2, 3, 4, 5, 6]
    bad = [6, 5, 4, 3, 2, 1]
    average = [2, 1, 5, 4, 6]
    print('A good time: {}'.format(timeit.timeit("merge_sort(good)", setup="from __main__ import merge_sort, good")))
    print('A bad time: {}'.format(timeit.timeit("merge_sort(bad)", setup="from __main__ import merge_sort, bad")))
    print('An average time: {}'.format(timeit.timeit("merge_sort(average)", setup="from __main__ import merge_sort, average")))