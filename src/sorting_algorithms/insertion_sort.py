"""Create an insertion sort algorithm."""


def insertion_sort(input):
    """Sort a given input with insertion sort."""
    for index in range(1, len(input)):
        value = input[index]
        prev = index - 1
        while prev >= 0:
            if value < input[prev]:
                input[prev + 1], input[prev] = input[prev], value
                prev -= 1
            else:
                break
    return input

if __name__ == '__main__':  # pragma: no cover
    import timeit
    good = [1, 2, 3, 4, 5, 6]
    bad = [6, 5, 4, 3, 2, 1]
    average = [2, 1, 5, 4, 6]
    print('A good time: {}'.format(timeit.timeit("insertion_sort(good)", setup="from __main__ import insertion_sort, good")))
    print('A bad time: {}'.format(timeit.timeit("insertion_sort(bad)", setup="from __main__ import insertion_sort, bad")))
    print('An average time: {}'.format(timeit.timeit("insertion_sort(average)", setup="from __main__ import insertion_sort, average")))