"""Test bubble sort for all it's sorted bubbliness."""
import pytest

def test_bubble_sort_can_be_imported():
    """Test import works okay."""
    from bubble_sort import bubble_sort
    assert bubble_sort


def test_bubble_sort_returns_three_values():
    """Test bubble sort with three numbers."""
    from bubble_sort import bubble_sort
    assert bubble_sort([6, 3, 7]) == [3, 6, 7]


def test_bubble_sort_returns_four_values():
    """Test bubble sort with four numbers."""
    from bubble_sort import bubble_sort
    assert bubble_sort([13, 6, 3, 7]) == [3, 6, 7, 13]


def test_bubble_sort_returns_five_values():
    """Test bubble sort with five numbers."""
    from bubble_sort import bubble_sort
    assert bubble_sort([13, 6, 3, 7, 1]) == [1, 3, 6, 7, 13]


def test_bubble_sort_returns_six_values():
    """Test bubble sort with six numbers."""
    from bubble_sort import bubble_sort
    assert bubble_sort([13, 5, 6, 3, 7, 1]) == [1, 3, 5, 6, 7, 13]


def test_bubble_sort_raises_error_with_string():
    """Test input error is raised if string is used."""
    from bubble_sort import bubble_sort
    with pytest.raises(TypeError):
        bubble_sort('sort this')
