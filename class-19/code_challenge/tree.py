from queue import Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class KArrTree:
    def __init__(self):
        self.root = None


def fizz_buzz(x):
    if x%3==0 and x%5==0:
        return 'FizzBuzz'
    elif x%3==0:
        return 'Fizz'
    elif x%5==0:
        return 'Buzz'
    else:
        return str(x)

def fizz_buzz_tree(k_ary_tree):
    # Logic for bfs of k_ary_tree
    fizzbuzz_values = []
    queue = Queue()
    queue.enqueue(k_ary_tree.root)
    while not queue.is_empty():
        node = queue.dequeue()
        fizzybuzzy = fizz_buzz(node.value)
        fizzbuzz_values.append(fizzybuzzy)
        for child in node.children:
            queue.enqueue(child)


# Way 1: Copy the tree before you start (Cloning), then go with Ahmad Zatar's solution
# Way 2: Build the new tree as you go through the loop


"""
             5
    2     4      8      9
 1 2 3  1 2 3  1 2 3  1 2 3
"""