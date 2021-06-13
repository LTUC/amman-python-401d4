# (5,6,2,5,1,3)

count_of_dice = {
    '1': 1,
    '2': 1,
    '3': 1,
    '4': 0,
    '5': 2,
    '6': 1
}

# count_of_dice['2'] => 1
# print(count_of_dice[7]) => Error


from collections import Counter

ctr = Counter((6,'a',5,1,5,3))

print(ctr)
# print(ctr[5])
# print(ctr[6])
# print(ctr['a'])
# print(ctr[4]) # No error here, value is 0
# print(ctr[7]) # Zero as well

# print(ctr.keys())
# print(ctr.values())
print(ctr.items())


print(ctr.most_common())
print(ctr.most_common(1))
print(ctr.most_common(1)[0][1])

print("Most common 1 of counter 2")
ctr2 = Counter((2,1,3,4,5,6))
print(ctr2.most_common(1)[0][1]) # score is 1500 points

