"""Test bubble sort for all it's sorted bubbliness."""
import pytest


def test_merge_sort_can_be_imported():
    """Test import works okay."""
    from merge_sort import merge_sort
    assert merge_sort


def test_merge_sort_returns_three_values():
    """Test merge sort with three numbers."""
    from merge_sort import merge_sort
    assert merge_sort([6, 3, 7]) == [3, 6, 7]


def test_merge_sort_returns_four_values():
    """Test merge sort with four numbers."""
    from merge_sort import merge_sort
    assert merge_sort([13, 6, 3, 7]) == [3, 6, 7, 13]


def test_merge_sort_returns_five_values():
    """Test merge sort with five numbers."""
    from merge_sort import merge_sort
    assert merge_sort([13, 6, 3, 7, 1]) == [1, 3, 6, 7, 13]


def test_merge_sort_returns_six_values():
    """Test merge sort with six numbers."""
    from merge_sort import merge_sort
    assert merge_sort([13, 5, 6, 3, 7, 1]) == [1, 3, 5, 6, 7, 13]


def test_merge_sort_raises_error_with_string():
    """Test input error is raised if string is used."""
    from merge_sort import merge_sort
    with pytest.raises(TypeError):
        merge_sort('sort this')
