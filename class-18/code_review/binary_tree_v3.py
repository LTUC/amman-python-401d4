from queue import Queue

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
    


def bfs(tree):
    # NO self CAN BE USED HERE because this is a function not a method

    # Create an empty queue
    queue = Queue()
    # get the root
    root = tree.root
    # equeue the root (start point)
    queue.enqueue(root)

    output = []
    # while loop that keeps going untill the queue is empty
    while not queue.is_empty():
        # dequeue and add to the output list
        node = queue.dequeue()
        output.append(node.value)
        # enqueue the left and right of the quequed node if it has
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    return output



if __name__=='__main__':
    tree = Tree()
    # Add nodes to the tree
    # call bfs
    bfs(tree)