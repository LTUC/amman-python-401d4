from binary_tree import __version__

from binary_tree.binary_tree import BinaryTree, Node

import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_pre_order(prepared_tree):
    assert prepared_tree.pre_order() == 'ABDECF'


def test_pre_order_empty_tree():
    tree = BinaryTree()
    assert tree.pre_order() == ''


@pytest.fixture
def prepared_tree():
    tree = BinaryTree()
    tree.root = Node('A')
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.left = Node('F')
    return tree
