import deque

class Queue:
    """Queue implementation using deque under the hood"""

    def __init__(self):
        self.storage = deque()

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.is_empty():
            raise EmptyError(self.dequeue)

        return self.storage.popleft()

    def peek(self):
        if self.is_empty():
            raise EmptyError(self.peek)

        return self.storage[0]

    def is_empty(self):
        return len(self.storage) == 0