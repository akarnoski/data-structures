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


# if __name__ == '__main__':