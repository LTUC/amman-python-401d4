class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
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


# Not valid Solution    
    # def pre_order_out_inclusive(self, output=''):
    #     if self.root:
    #         output += self.root.value
    #     self.root.left.pre_order_out_inclusive(output)
    #     self.root.right.pre_order_out_inclusive(output)
    #     return output


# Issue 1: pre_order works for Tree instance not Node instance
# Issue 2: output will be reset every function call
# Solution: USe a closure (Define a function inside a function)





# x = 9

# def add_to_global(y):
#     global x
#     x = x+y

# add_to_global(5)

# print(x)