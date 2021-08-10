# def gen(x):
#     for i in range(x):
#         try:
#             yield i
#         except StopIteration:
#             break


# num_gen = gen(5)
# for num in num_gen:
#     print(next(num))

# from linked_list import LinkedList

# ll = LinkedList(['a','b','c','d'])
# for item in ll:
#     print(item)


# letters_caps = [letter.upper() for letter in ll]
# print(letters_caps)


# ll_nums = [1,2,3,4,5,6,7,8,9]

# even_nums = [num for num in ll_nums if num%2==0]
# print(even_nums)


# from functools import wraps

# def lowerize(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         original_value = func(*args, **kwargs)
#         return original_value.lower()
#     return wrapper


# def camelize(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         original_value = func(*args, **kwargs)
#         camel = ''
#         for word in original_value.split():
#             new_word = word[0].upper() + word[1:]
#             camel += new_word + ' '
#         return camel
#     return wrapper


# @camelize
# @lowerize
# def fun_with_words(noun1, noun2, verb1):
#     return f'{noun1}s love to {verb1} all the {noun2}s'

# print(fun_with_words('Cat','CARROT','sIng'))