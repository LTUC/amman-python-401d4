# head -> 5 -> 8 -> None
from abc import abstractmethod
from linked_list import LinkedList

ll = LinkedList(['a','b','c','d','f'])
ll2 = LinkedList(['a','b','c','d','f'])

print(ll == ll2) # Equality in length
# Alternative to:
# ll = LinkedList()
# ll.insert('a')
# ll.insert('b')
# ll.insert('c')
# ll.insert('d')
# ll.insert('f')


# for item in ll:
#     print(item)


# print(ll)
# print(len(ll))



# Generator
# def gen(x):
#     for i in range(x):
#         yield i

# nums_gen = gen(5)
# print(next(nums_gen))
# print(next(nums_gen))
# print(next(nums_gen))
# print(next(nums_gen))
# print(next(nums_gen))
# print(next(nums_gen)) Error

from functools import wraps

def lowerize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_output = func(*args, **kwargs)
        return original_output.lower()
    return wrapper


def camelize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        original_output = func(*args, **kwargs)
        return ' '.join([word.capitalize() for word in original_output.split()])
        
        # Cats love to sinG all the CARROTs
        # output = ''
        # for word in original_output.split():
        #     new_word = word.capitalize()
        #     # new_word = word[0].upper() + word[1:]
        #     output += new_word + ' '
        # return output
    return wrapper



@camelize
@lowerize
def funny_words(noun1, noun2, verb):
    return f'{noun1}s love to {verb} all the {noun2}s'


print(funny_words('Cat', 'CARROT', 'sinG'))

#Alternatively
print('hello CLASS lets pLAY'.title())