"""Test trie tree data structure."""
import pytest


def test_trie_tree_ficture(tt_fixture):
    """Test there's working trie tree fixture."""
    assert tt_fixture


def test_trie_tree_size_is_zero(tt_fixture):
    """Test on initialization size is zero."""
    assert tt_fixture.size == 0


def test_trie_tree_root(tt_fixture):
    """Test trie tree root on initialization."""
    assert tt_fixture.root.val == '*'


def test_trie_tree_insert_size_is_one(tt_fixture):
    """Test trie tree insert doesn't raise error and size becomes one."""
    new_word = tt_fixture.insert('word')
    assert tt_fixture.size == 1


def test_trie_tree_insert_using_helper(tt_fixture):
    """Test trie tree insert with tree crawler helper function."""
    new_word = tt_fixture.insert('word')
    assert tt_fixture._val_crawler('word') == ['*', 'w', 'o', 'r', 'd', '$']


def test_trie_tree_helper_raises_error(tt_fixture):
    """Test helper function raises error on word not in trie tree."""
    with pytest.raises(KeyError):
        tt_fixture._val_crawler('word')


def test_node_helper_function(tt_fixture):
    """Test trie tree insert with tree crawler helper function."""
    from trie_tree import Node
    new_word = tt_fixture.insert('word')
    node_list = tt_fixture._node_crawler('word')
    for node in node_list:
        assert isinstance(node, Node)


def test_node_helper_function_allows_access_to_val(tt_fixture):
    """Test node helper function allows access to the values."""
    from trie_tree import Node
    new_word = tt_fixture.insert('word')
    node_list = tt_fixture._node_crawler('word')
    assert node_list[1].val == 'w'


def test_trie_tree_node_helper_raises_error(tt_fixture):
    """Test helper function raises error on word not in trie tree."""
    with pytest.raises(KeyError):
        tt_fixture._node_crawler('word')


def test_size_returns_size_with_one_word(tt_fixture):
    """Test size returns one after one word inserted."""
    new_word = tt_fixture.insert('word')
    assert tt_fixture.size == 1


def test_size_with_random_words(tt_fixture):
    """Testing size on random words insterted."""
    tt_fixture.insert('word')
    tt_fixture.insert('bologna')
    tt_fixture.insert('elephant')
    tt_fixture.insert('therapy')
    assert tt_fixture.size == 4


def test_size_returns_size_stays_same_for_same_word(tt_fixture):
    """Test size stays the same if word is added again."""
    new_word = tt_fixture.insert('word')
    second_word = tt_fixture.insert('word')
    assert tt_fixture.size == 1


def test_size_returns_size_changes_with_single_difference(tt_fixture):
    """Test size is updated with single letter difference."""
    new_word = tt_fixture.insert('word')
    second_word = tt_fixture.insert('words')
    assert tt_fixture.size == 2


def test_size_returns_size_when_word_is_smaller(tt_fixture):
    """Test size is updated with single letter difference."""
    new_word = tt_fixture.insert('words')
    second_word = tt_fixture.insert('word')
    assert tt_fixture.size == 2


def test_contains_returns_true_for_word_in_tree(tt_fixture):
    """Test contains method returns true is word is in tree."""
    new_word = tt_fixture.insert('word')
    assert tt_fixture.contains('word')


def test_contains_returns_false_for_word_not_in_tree(tt_fixture):
    """Test contains method returns false is word is not in tree."""
    assert tt_fixture.contains('banana') is False


def test_contains_returns_false_for_word_with_letter_difference(tt_fixture):
    """Test contains method returns false from letter difference."""
    tt_fixture.insert('banana')
    assert tt_fixture.contains('bananas') is False


def test_contains_returns_false_for_word_apart_of_another_word(tt_fixture):
    """Test contains method returns false from letter difference."""
    tt_fixture.insert('bananas')
    assert tt_fixture.contains('banana') is False