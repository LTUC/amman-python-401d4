a = [7,3,8,9]

# Enqueue
a.append(-2) # O(1)
# a = [7,3,8,9,-2]


# Dequeue
a.pop(0) # O(1)
# returns 7
# a = [3,8,9,-2]


"""
a = [7,3,8,9]

In memory:
.............begin a here at 3000...........
............ 3000 3001 3002 3003 3004 3005 3006 3007 ..........
.............7    3    8    9  ...............
.............7    3    8    9    -2  ......... append(-2)
............empty 3    8    9    -2  ......... pop(0)
a[0] => empty while it should return 3
next time I dequeue pop(0) => return nothing


Fixing:
............ 3000 3001 3002 3003 3004 3005 3006 3007 ..........
.............3    8    9    -2  ......... O(n)
"""