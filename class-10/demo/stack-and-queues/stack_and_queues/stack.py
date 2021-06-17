from stack_and_queues.node import Node

class Stack:
    def __init__(self):
        self.top = None
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
    def pop(self):
        pass
    def peek(self):
        pass
    def is_empty(self): 
        return self.top == None
        # OR
        # return True if self.top is None else False
        # OR
        # if self.top is None:
        #     return True
        # return False



# 11:30 we come back

# If we use a list(array), easily do this:
# data = [3, -7, 'd']
# data.pop()
# data.append(5)
# data[-1]
# return if len(data) == 0
