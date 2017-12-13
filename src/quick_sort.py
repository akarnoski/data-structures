"""Function for the quick sort alogorithm."""


def quick_sort(in_list):
    """Quick sort function."""
    if not isinstance(in_list, list):
        raise TypeError('Please insert a list')
    if len(in_list) <= 1:
        return in_list
    else:
        pivot = in_list[0]
        i = 0
        for x in range(len(in_list) - 1):
            if in_list[x + 1] < pivot:
                in_list[x + 1], in_list[i + 1] = in_list[i + 1], in_list[x + 1]
                i += 1
        in_list[0], in_list[i] = in_list[i], in_list[0]
        small_stuff = quick_sort(in_list[:i + 1])
        big_stuff = quick_sort(in_list[i + 1:])
        return small_stuff + big_stuff


if __name__ == '__main__':  # pragma: no cover
    import timeit
    good = [1, 2, 3, 4, 5, 6]
    bad = [6, 5, 4, 3, 2, 1]
    average = [2, 1, 5, 4, 6]
    print('A good time: {}'.format(timeit.timeit("quick_sort(good)", setup="from __main__ import quick_sort, good")))
    print('A bad time: {}'.format(timeit.timeit("quick_sort(bad)", setup="from __main__ import quick_sort, bad")))
    print('An average time: {}'.format(timeit.timeit("quick_sort(average)", setup="from __main__ import quick_sort, average")))