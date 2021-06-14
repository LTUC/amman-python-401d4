# insert_before
"""
"""



# insert_after
"""
1. Define a method in LinkedList class named "insert_after", takes in item we insert after and the inserted value
2. Loop over the LL from head to None
    2.a. Check if current value ?= tergeted value
        - yes: stop
        - no: move on
    2.b. 
        - Node(value).next = current.next
        - current.next = Node(value)


insert_after('s', -1)

head - 4 -> 7 -> 's' -> 19 -> None
current = Node('s')

head - 4 -> 7 -> 's' -> -1 -> 19 -> None


To test:

expected = -1
actual = ll.head.next.next.next.value
assert expected == actual
"""


