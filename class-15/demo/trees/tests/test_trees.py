from trees import __version__

from trees.tree import Tree, Node

import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_pre_order(prepared_tree):
    assert prepared_tree.pre_order() == 'ABDECF'


def test_pre_order_empty_tree():
    tree = Tree()
    assert tree.pre_order() == ''

# def test_pre_order_inclusive(prepared_tree):
#     assert prepared_tree.pre_order_out_inclusive() == 'ABDECF'





@pytest.fixture
def prepared_tree():
    tree = Tree()
    tree.root = Node('A')
    tree.root.left = Node('B')
    tree.root.right = Node('C')
    tree.root.left.left = Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.left = Node('F')
    return tree
