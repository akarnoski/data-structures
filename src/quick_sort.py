"""Function for the quick sort alogorithm."""


def quick_sort(input):
    """Quick sort function."""
    if not isinstance(input, list):
        raise TypeError('Please insert a list')
    if len(input) <= 1:
        return input
    else:
        pivot = input[0]
        i = 0
        for x in range(len(input) - 1):
            if input[x + 1] < pivot:
                input[x + 1], input[i + 1] = input[i + 1], input[x + 1]
                i += 1
                print(i)
        input[0], input[i] = input[i], input[0]
        small_stuff = quick_sort(input[:i + 1])
        big_stuff = quick_sort(input[i + 1:])
        return small_stuff + big_stuff


if __name__ == '__main__':  # pragma: no cover
    import timeit
    good = [1, 2, 3, 4, 5, 6]
    bad = [6, 5, 4, 3, 2, 1]
    average = [2, 1, 5, 4, 6]
    print('A good time: {}'.format(timeit.timeit("quick_sort(good)", setup="from __main__ import quick_sort, good")))
    print('A bad time: {}'.format(timeit.timeit("quick_sort(bad)", setup="from __main__ import quick_sort, bad")))
    print('An average time: {}'.format(timeit.timeit("quick_sort(average)", setup="from __main__ import quick_sort, average")))