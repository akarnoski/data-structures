"""Test insertion sort for all it's sorted bubbliness."""
import pytest


def test_insertion_sort_can_be_imported():
    """Test import works okay."""
    from insertion_sort import insertion_sort
    assert insertion_sort


def test_insertion_sort_returns_three_values():
    """Test insertion sort with three numbers."""
    from insertion_sort import insertion_sort
    assert insertion_sort([6, 3, 7]) == [3, 6, 7]


def test_insertion_sort_returns_four_values():
    """Test insertion sort with four numbers."""
    from insertion_sort import insertion_sort
    assert insertion_sort([13, 6, 3, 7]) == [3, 6, 7, 13]


def test_insertion_sort_returns_five_values():
    """Test insertion sort with five numbers."""
    from insertion_sort import insertion_sort
    assert insertion_sort([13, 6, 3, 7, 1]) == [1, 3, 6, 7, 13]


def test_insertion_sort_returns_six_values():
    """Test insertion sort with six numbers."""
    from insertion_sort import insertion_sort
    assert insertion_sort([13, 5, 6, 3, 7, 1]) == [1, 3, 5, 6, 7, 13]


def test_insertion_sort_raises_error_with_string():
    """Test input error is raised if string is used."""
    from insertion_sort import insertion_sort
    with pytest.raises(TypeError):
        insertion_sort('sort this')
