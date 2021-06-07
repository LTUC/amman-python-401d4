def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)



# Alternative solution using while loop

# def fact(n):
#     result = 1
#     temp = n
#     while temp>1:
#         result *= temp
#         temp -= 1
#     return result


