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
    thing = [1, 2, 3, 4, 5, 6]
    mycode = insertion_sort(thing)
    t = timeit.Timer(insertion_sort(thing))
    print(t.timeit())
