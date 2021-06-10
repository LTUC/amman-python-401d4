from linked_list.linked_list import LinkedList
from linked_list import __version__
from linked_list.linked_list import LinkedList

def test_version():
    assert __version__ == '0.1.0'

def test_append_1():
    ll = LinkedList()
    ll.append(1)
    assert ll.head.value == 1

