from linked_list.linked_list import LinkedList
from linked_list import __version__
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_append_1():
    ll = LinkedList()
    ll.append(1)
    assert ll.head.value == 1

def test_append_5_values(prepared_ll):
    assert prepared_ll.head.value == 4
    assert prepared_ll.head.next.value == 7
    assert prepared_ll.head.next.next.value == 'd'
    assert prepared_ll.head.next.next.next.value == None
    assert prepared_ll.head.next.next.next.next.value == 'hello'

def test_repr(prepared_ll):
    assert prepared_ll.__repr__() == '4 - 7 - d - None - hello'




@pytest.fixture
def prepared_ll():
    ll = LinkedList()
    ll.append(4)
    ll.append(7)
    ll.append('d')
    ll.append(None)
    ll.append('hello')
    return ll
