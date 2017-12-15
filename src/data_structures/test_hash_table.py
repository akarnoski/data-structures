"""Test functions for Hash Table module.

The hash table fixture initializes a table with 20 slots in it,

All tests based off the ht_fixture assume the user has assigned a fixed size.

Any test including the initialization of a hash table manually

are too assume a different input."""

import pytest


def test_manual_creation_of_ht_fixture_with_no_arguments():
    """Test hash table fixture works with no arguments."""
    from hash_table import HashTable
    ht = HashTable()
    assert isinstance(ht, HashTable)


def test_manual_creation_of_ht_fixture_with_size_argument():
    """Test hash table fixture works with size argument."""
    from hash_table import HashTable
    ht = HashTable(20)
    assert isinstance(ht, HashTable)


def test_ht_fixture_works(ht_fixture):
    """Test hash table fixture works."""
    assert ht_fixture


def test_ht_fixture_has_correct_buckets(ht_fixture):
    """Test hash table fixture works."""
    assert ht_fixture.buckets == 20


def test_ht_manual_without_size_has_no_buckets():
    """Test hash table without size argument has no buckets on initialization."""
    from hash_table import HashTable
    ht = HashTable()
    assert ht.buckets is None


def test_ht_fixture_has_correct_available(ht_fixture):
    """Test hash table fixture works."""
    assert ht_fixture.available == 20


def test_ht_manual_without_size_has_zero_available():
    """Test hash table without size argument has zero available."""
    from hash_table import HashTable
    ht = HashTable()
    assert ht.available == 0


def test_ht_fixture_size_with_nothing_set_is_zero(ht_fixture):
    """Test hash table fixture works."""
    assert ht_fixture.size == 0


def test_ht_manual_size_with_nothing_set_is_zero():
    """Test hash table without size argument has zero available."""
    from hash_table import HashTable
    ht = HashTable()
    assert ht.size == 0


def test_hash_fuction_returns_additative_value_lowercase(ht_fixture):
    """Test the hash function returns and additive value."""
    word = 'word'
    word_value = 0
    for letter in word:
        word_value += ord(letter)
    assert ht_fixture._hash('word') == word_value


def test_hash_fuction_returns_additative_value_uppercase(ht_fixture):
    """Test the hash function returns and additive value."""
    word = 'WORD'
    word_value = 0
    for letter in word:
        word_value += ord(letter)
    assert ht_fixture._hash('WORD') == word_value


def test_hash_fuction_raises_error_if_key_is_int(ht_fixture):
    """Test the hash function raises a type error if key is number."""
    with pytest.raises(TypeError):
        ht_fixture._hash(30)


def test_hash_fuction_raises_error_if_key_is_bool(ht_fixture):
    """Test the hash function raises a type error if key is boolean."""
    with pytest.raises(TypeError):
        ht_fixture._hash(False)


def test_index_helper_returns_expected_index(ht_fixture):
    """Test the hash function raises a type error if key is boolean."""
    assert ht_fixture._index_helper('word') == 4


def test_set_fuction_stores_value_with_give_key(ht_fixture):
    """Test set function sets key and value."""
    ht_fixture.set('word', 'this is my value')
    index_location = ht_fixture._index_helper('word')
    long_ass_search = ht_fixture.table[index_location].search('word').val
    assert long_ass_search == 'this is my value'


def test_set_fuction_stores_second_value_with_give_key(ht_fixture):
    """Test set fuctions sets key and value in index with previous value."""
    ht_fixture.set('rowd', 'this is my first value')
    ht_fixture.set('word', 'this is my second value')
    index_location = ht_fixture._index_helper('word')
    long_ass_search = ht_fixture.table[index_location].search('word').val
    assert long_ass_search == 'this is my second value'


def test_get_fuction_returns_value_of_requested_key(ht_fixture):
    """Test get function returns value of the requested key."""
    ht_fixture.set('word', 'this is my second value')
    assert ht_fixture.get('word') == 'this is my second value'


def test_get_fuction_returns_value_with_multiple_possibilites(ht_fixture):
    """Test get function returns correct value when multiple keys are stored
    at same index in table."""
    ht_fixture.set('rowd', 'this is my first value')
    ht_fixture.set('word', 'this is my second value')
    assert ht_fixture.get('word') == 'this is my second value'