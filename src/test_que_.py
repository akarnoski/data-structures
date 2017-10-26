import pytest


def test_queue_is_instance_of_dll_object():
    """Test stack is instance of Stack()."""
    from que_ import Queue
    q = Queue()
    assert isinstance(q, Queue)
