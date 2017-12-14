"""Test sorting alorithms for correct outputs."""
import pytest


"""
Basic Tests

Checking to make sure each sort can be imported without errors.

"""


def test_bubble_sort_can_be_imported():
    """Test import works okay."""
    from bubble_sort import bubble_sort
    assert bubble_sort


def test_quick_sort_can_be_imported():
    """Test import works okay."""
    from quick_sort import quick_sort
    assert quick_sort


"""
Functionality Tests

Testing that each sort returns the correct solution.

"""


SUPER_TEST = [
    ([6, 3, 7], [3, 6, 7]),
    ([13, 6, 3, 7], [3, 6, 7, 13]),
    ([13, 6, 3, 7, 1], [1, 3, 6, 7, 13]),
    ([13, 5, 6, 3, 7, 1], [1, 3, 5, 6, 7, 13]),
    ([5, 3], [3, 5]),
    ([1], [1]),
    ([29, 32, 40, 25, 50, 27, 31, 37], [25, 27, 29, 31, 32, 37, 40, 50]),
    ([226, 401, 291, 290, 27, 427, 477, 326], [27, 226, 290, 291, 326, 401, 427, 477]),
    ([18, 16, 17, 19, 15], [15, 16, 17, 18, 19])
]


@pytest.mark.parametrize("num_list, result", SUPER_TEST)
def test_bubble_sort_returns_correct_list(num_list, result):
    """Test bubble sort returns a properly sorted list."""
    from bubble_sort import bubble_sort
    assert bubble_sort(num_list) == result


@pytest.mark.parametrize("num_list, result", SUPER_TEST)
def test_quick_sort_returns_correct_list(num_list, result):
    """Test quick sort returns a properly sorted list."""
    from quick_sort import quick_sort
    assert quick_sort(num_list) == result


@pytest.mark.parametrize("num_list, result", SUPER_TEST)
def test_radix_sort_returns_correct_list(num_list, result):
    """Test radix sort returns a properly sorted list."""
    from radix_sort import radix_sort
    assert radix_sort(num_list) == result


"""
Error Handling

Test that each sort raises error when appropriate.
"""


def test_bubble_sort_raises_error_with_string():
    """Test input error is raised if string is used."""
    from bubble_sort import bubble_sort
    with pytest.raises(TypeError):
        bubble_sort('sort this')


def test_quick_sort_raises_error_with_string():
    """Test input error is raised if string is used."""
    from quick_sort import quick_sort
    with pytest.raises(TypeError):
        quick_sort('sort this')


def test_bubble_sort_raises_error_with_string():
    """Test input error is raised if string is used."""
    from bubble_sort import bubble_sort
    with pytest.raises(TypeError):
        bubble_sort('sort this')