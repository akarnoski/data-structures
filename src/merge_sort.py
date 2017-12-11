"""Create an merge sort algorithm."""


def merge_sort(input):
    """Sort a given input with merge sort."""
    if not isinstance(input, list):
        raise TypeError('Please insert a list')
    if len(input) == 1:
        return input
    if len(input) == 2:
        if input[0] > input[1]:
            input[0], input[1] = input[1], input[0]
        return input
    else:
        half = int(len(input) / 2)
        one_half = merge_sort(input[:half])
        two_half = merge_sort(input[half:])
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