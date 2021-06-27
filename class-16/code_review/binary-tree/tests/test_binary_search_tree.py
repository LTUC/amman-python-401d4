from binary_tree.binary_search_tree import BinarySearchTree
from binary_tree.binary_tree import Node

import pytest

def test_add_to_root():
    # loop to add
    # check items
    bst = BinarySearchTree()
    bst.add(7)
    assert bst.root.value == 7
    assert bst.root.right == None

def test_add_multiple():
    bst = BinarySearchTree()
    values = [15, 7, 2, 13, 10, 35, 23, 17, 40]
    for value in values:
        bst.add(value)
    assert bst.root.right.value == 35
    assert bst.root.left.right.left.value == 10
    assert bst.root.left.right.left.right == None


@pytest.mark.skip()
def test_contains(bst):
    # Add first (not recommended to use the add method)
    # check if contains
    assert bst.contains(7) == True
    assert bst.conatins(99) == False
    assert bst.conatins(10) == True


@pytest.fixture
def bst():
    bst = BinarySearchTree()
    bst.root = Node(15)
    bst.root.left = Node(7)
    bst.root.right = Node(35)
    bst.root.right.right = Node(40)
    bst.root.right.left = Node(23)
    bst.root.right.left.left = Node(17)
    bst.root.left.left = Node(2)
    bst.root.left.right = Node(13)
    bst.root.left.right.left = Node(10)
    return bst






# See you at 10:05

"""

                 15
      7                      35
2           13          23         40
         10          17


[15 7 2 13 10 35 23 17 40]

"""