"""Test functions for Binary Search Tree module."""
import pytest


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
    """Test size of binary search tree is one."""
    bst_fixture.insert(23)
    bst_fixture.insert(13)
    bst_fixture.insert(5)
    assert bst_fixture.size() == 3


def test_includes_returns_true_with_inserted_node(bst_fixture):
    """Test searching for node returns node with value."""
    bst_fixture.insert(23)
    contains = bst_fixture.contains(23)
    assert contains

