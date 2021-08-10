from abc import abstractclassmethod


class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

class LinkedList:

    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection): # [a,b,c] => [a] -> [b] -> [c] -> None
                self.insert(item)


    def __str__(self):
        out = "head -> "
        for value in self:
            out += f"[ {value} ] -> "
        return out + "None"

    # def __str__(self):
    #     # head -> node1 -> node2 -> .... -> noden -> None
    #     output = "head -> "
    #     current = self.head
    #     while current:
    #         output += f'{str(current.value)} -> '
    #         current = current.next
    #     output += 'None'
    #     return output

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):

        node = Node(value)

        if not self.head:
            self.head = node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = node

    def __iter__(self):
        def values_gen():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return values_gen()

    def __len__(self):
        return len(list(iter(self)))
    
    def __eq__(self, other):
        return len(self) == len(other)