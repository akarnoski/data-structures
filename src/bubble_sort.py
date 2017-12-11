"""Create a bubble sort algorithm."""


def bubble_sort(input):
    """Function to run the bubble sort algorithm."""
    if not isinstance(input, list):
        raise TypeError('Please insert a list')
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(input) - 1):
            if input[i] > input[i + 1]:
                input[i], input[i + 1] = input[i + 1], input[i]
                swapped = True
    return input


if __name__ == '__main__':  # pragma: no cover
    import timeit
    good = [1, 2, 3, 4, 5, 6]
    bad = [6, 5, 4, 3, 2, 1]
    average = [2, 1, 5, 4, 6]
    print('A good time: {}'.format(timeit.timeit("bubble_sort(good)", setup="from __main__ import bubble_sort, good")))
    print('A bad time: {}'.format(timeit.timeit("bubble_sort(bad)", setup="from __main__ import bubble_sort, bad")))
    print('An average time: {}'.format(timeit.timeit("bubble_sort(average)", setup="from __main__ import bubble_sort, average")))