"""Test quick sort for all it's sorted quickness."""
import pytest

def test_quick_sort_can_be_imported():
    """Test import works okay."""
    from quick_sort import quick_sort
    assert quick_sort


def test_quick_sort_returns_three_values():
    """Test quick sort with three numbers."""
    from quick_sort import quick_sort
    assert quick_sort([6, 3, 7]) == [3, 6, 7]


def test_quick_sort_returns_four_values():
    """Test quick sort with four numbers."""
    from quick_sort import quick_sort
    assert quick_sort([13, 6, 3, 7]) == [3, 6, 7, 13]


def test_quick_sort_returns_five_values():
    """Test quick sort with five numbers."""
    from quick_sort import quick_sort
    assert quick_sort([13, 6, 3, 7, 1]) == [1, 3, 6, 7, 13]


def test_quick_sort_returns_six_values():
    """Test quick sort with six numbers."""
    from quick_sort import quick_sort
    assert quick_sort([13, 5, 6, 3, 7, 1]) == [1, 3, 5, 6, 7, 13]


def test_quick_sort_raises_error_with_string():
    """Test input error is raised if string is used."""
    from quick_sort import quick_sort
    with pytest.raises(TypeError):
        quick_sort('sort this')