from binary_tree.binary_tree import BinaryTree, Node

# See you at 11:11

class BinarySearchTree(BinaryTree):
    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        def _traverse(node, value): # O(log n)
            # if no root, add to the root
            # if value <= root.value add to the left
            # if value > root.value add to the right
            if value <= node.value:
                if not node.left:
                    node.left = Node(value)
                    return
                else:
                    _traverse(node.left, value)
            else:
                if not node.right:
                    node.right = Node(value)
                    return
                else:
                    _traverse(node.right, value)
        
        _traverse(self.root, value)




    def contains(self):
        pass



if __name__=='__main__':
    bst = BinarySearchTree()
    bst.root = Node(15)
    assert bst.root.value == 15
    print("All passed fine!!!")





"""
26 26
            26
        



"""