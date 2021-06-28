class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        # Initialize the output
        output = ''
        if not self.root:
            return output

        # Define a closure function to be used internally
        def _traverse(node):
            nonlocal output # Because output is not accessible
            output = output + str(node.value) # Root

            # if left, call the function recursively for root.left
            if node.left:
                _traverse(node.left)
            # if right, call the function recursively for root.right
            if node.right:
                _traverse(node.right)
            return output
        
        # Call the closure function with root
        _traverse(self.root)

        # Return the output
        return output
    
    
    def max_value(self):
        
        """
        Way 1: 
        Traverse the tree O(n)
        Output will be an array
        find max in the array O(n)
        Space: O(n)

        Way 2:
        Consider root to be max value O(1)
        traverse the tree O(n)
         keep comparing with the max
        Space: O(1)

        
        """
