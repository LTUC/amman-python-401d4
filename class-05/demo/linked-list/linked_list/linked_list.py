class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
Draft:

ll: head - None

ll.append(4)
ll: head - Node(4) -> None

ll.append(-1)
ll: head - Node(4) -> Node(-1) -> None

ll.append('s')
ll: head - Node(4) -> Node(-1) -> Node('s') -> None
"""


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        Adds a node of a value to the head of LL
        """
        pass

    def append(self, value):
        """
        Adds a node of a value to the end of LL
        """
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node


    def include(self, value):
        """
        Return T/F if value is in the linked list or not
        """
        pass
    
    def __str__(self):
        # "{ a } -> { b } -> { c } -> NULL"
        # Loop over all nodes
        # print all values in one line
        pass

    def __repr__(self):
        pass

    


if __name__ == "__main__":
    # Instances of Node
    n1 = Node(34)
    n2 = Node('Suhaib')
    n3 = Node(True)
    print(n2.value)


    ll = LinkedList()
    # Value of first node on head
    ll.append(4)
    # next of head (next of Node(4)) is Null
    ll.append(-1)
    ll.append('s')
    # I have ll: head - Node(4) -> Node(-1) -> Node('s') -> None
    print(ll.head.value)
    print(ll.head.next.value)
    print(ll.head.next.next.value)



    


