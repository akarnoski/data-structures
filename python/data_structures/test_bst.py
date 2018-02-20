"""Test functions for Binary Search Tree module."""
import pytest


def test_bst_fixture_works(bst_fixture):
    """Test binary search tree root is inserted node."""
    assert bst_fixture


def test_bst_insert_node(bst_fixture):
    """Test binary search tree root is inserted node."""
    bst_fixture.insert(13)
    assert bst_fixture.root.val == 13


def test_lower_inserted_node_become_left(bst_fixture):
    """Test lower inserted node becomes left node."""
    bst_fixture.insert(13)
    bst_fixture.insert(7)
    assert bst_fixture.root.left.val == 7


def test_higher_inserted_node_become_right(bst_fixture):
    """Test higher inserted node becomes right node."""
    bst_fixture.insert(13)
    bst_fixture.insert(23)
    assert bst_fixture.root.right.val == 23


def test_search_for_inserted_node(bst_fixture):
    """Test searching for node returns node with value."""
    bst_fixture.insert(23)
    search = bst_fixture.search(23)
    assert search.val == 23


def test_search_returns_none_if_no_node(bst_fixture):
    """Test searching for node returns node with value."""
    search = bst_fixture.search(23)
    assert search is None


def test_search_for_inserted_node_with_multiple_nodes(bst_fixture):
    """Test searching for node returns node with value."""
    bst_fixture.insert(23)
    bst_fixture.insert(13)
    bst_fixture.insert(5)
    search = bst_fixture.search(13)
    assert search.val == 13


def test_size_for_empty_tree_returns_zero(bst_fixture):
    """Test size of empty binary search tree is zero."""
    assert bst_fixture.size() == 0


def test_size_for_tree_returns_one(bst_fixture):
    """Test size of binary search tree is one."""
    bst_fixture.insert(13)
    assert bst_fixture.size() == 1


def test_size_for_buncho_node_tree_returns_three(bst_fixture):
    """Test size of binary search tree is three."""
    bst_fixture.insert(23)
    bst_fixture.insert(13)
    bst_fixture.insert(5)
    assert bst_fixture.size() == 3


def test_returned_depth_for_left_side_only(bst_fixture):
    """Test depth returns two with nodes on left side."""
    bst_fixture.insert(5)
    bst_fixture.insert(13)
    bst_fixture.insert(23)
    assert bst_fixture.depth() == 2


def test_returned_depth_for_right_side_only(bst_fixture):
    """Test depth returns two with nodes on right side."""
    bst_fixture.insert(5)
    bst_fixture.insert(3)
    bst_fixture.insert(1)
    assert bst_fixture.depth() == 2


def test_returned_depth_with_both_sides(bst_fixture):
    """Test depth returns two with nodes on both sides."""
    bst_fixture.insert(5)
    bst_fixture.insert(13)
    bst_fixture.insert(3)
    assert bst_fixture.depth() == 1


def test_returns_zero_depth_when_no_nodes(bst_fixture):
    """Test depth returns zero if there are no nodes in tree."""
    assert bst_fixture.depth() == 0


def test_includes_returns_true_with_inserted_node(bst_fixture):
    """Test searching for node returns node with value."""
    bst_fixture.insert(23)
    contains = bst_fixture.contains(23)
    assert contains


def test_includes_returns_true_with_inserted_node(bst_fixture):
    """Test searching for node returns node with value."""
    contains = bst_fixture.contains(23)
    assert contains is False


def test_bst_takes_in_iterable():
    """Test binary search tree takes an iterable."""
    from bst import BinarySearchTree
    tree = BinarySearchTree([7, 13, 23])
    assert tree.root.val == 7


def test_returned_balance_with_both_sides(bst_fixture):
    """Test balance is zero when both sides are same depth."""
    bst_fixture.insert(5)
    bst_fixture.insert(13)
    bst_fixture.insert(3)
    assert bst_fixture.balance() == 0


def test_returned_balance_with_right_side(bst_fixture):
    """Test balance is negative when depth is greater on right side."""
    bst_fixture.insert(5)
    bst_fixture.insert(13)
    bst_fixture.insert(23)
    assert bst_fixture.balance() == -2


def test_returned_balance_with_left_side(bst_fixture):
    """Test balance is positive when depth is greater on right left."""
    bst_fixture.insert(15)
    bst_fixture.insert(3)
    bst_fixture.insert(7)
    bst_fixture.insert(23)
    bst_fixture.insert(13)
    assert bst_fixture.balance() == 2


def test_balance_returns_zero_if_tree_is_empty(bst_fixture):
    """Test balance is positive when depth is greater on right left."""
    assert bst_fixture.balance() == 0

def test_get_node_method(bst_fixture):
    """Test get node returns node it searches for."""
    bst_fixture.insert(15)
    bst_fixture.insert(3)
    bst_fixture.insert(7)
    bst_fixture.insert(23)
    bst_fixture.insert(13)
    assert bst_fixture.get_node(3).val == 3
