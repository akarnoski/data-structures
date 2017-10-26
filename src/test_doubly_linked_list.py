import pytest


def test_node_has_attributes():
    """Test that the node has attributes."""
    from doubly_linked_list import Node
    n = Node(1, None)
    assert n.data
    assert n.next_node is None
    assert n.previous_node is None


def test_double_linked_list_has_head():
    """test if the linked list has head node."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    assert dll.head is None


def test_double_linked_list_push_adds_new_item():
    """test that if new node is added."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    dll.push('val')
    assert dll.head.data == 'val'


def test_double_linked_list_push_two_last_value_is_head():
    """test that two nodes are added."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    dll.push('val')
    dll.push('val2')
    assert dll.head.data == 'val2'


def test_double_linked_list_moves_old_head_to_next():
    """test that the new node is moved to head."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    dll.push('val')
    dll.push('val2')
    assert dll.head.next_node.data == 'val'


def test_double_linked_list_pop_removes_head_returns_value():
    """test pop removes head."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    dll.push('potato')
    dll.pop()
    assert dll.head is None


def test_double_linked_list_pop_returns_head_value():
    """test pop returns value."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    dll.push('potato')
    output = dll.pop()
    assert output == 'potato'


def test_double_linked_list_pop_shifts_head_properly():
    """test pop shifts head."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    dll.push('potato')
    dll.push('cabbage')
    dll.pop()
    assert dll.head.data == 'potato'


@pytest.fixture
def test_double_linked_list_pop_empty_raises_exception():
    """test pop on empty linked list raises exception."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    with pytest.raises(IndexError):
        dll.pop()


@pytest.fixture
def test_size_method_returns_list_length():
    """test size method on linked list."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    assert dll.size() == 0


@pytest.mark.parametrize('n', range(100))
def test_size_method_returns_list_length2(n):
    """test size method on linked list."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    for i in range(n):
        dll.push(i)
    assert dll.size() == n


def test_double_linked_list_append_value():
    """test double linked list appends value to tail."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    for i in range(5):
        dll.push(i)
    dll.append(6)
    tail = dll.tail.data
    assert tail == 6


def test_double_linked_list_shift_method():
    """test double linked list removes last value."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    for i in range(5):
        dll.push(i)
    dll.shift()
    tail = dll.tail.data
    assert tail == 1
