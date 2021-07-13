a = [5,1,8,3,9,10,15,4]

def merge_sort():
    pass

merge_sort(a)
merge_sort([5,1,8,3,9,10,15,4])

n = 8
mid = 4
left = [5,1,8,3]
right = [9,10,15,4]




"""
Call merge_sort([5,1,8,3,9,10,15,4])
    1. merge_sort([5,1,8,3])

        1.1 merge_sort([5,1]) => returns [1,5]
            1.1.1 merge_sort([5])

            1.1.2 merge_sort([1])

            1.1.3 merge([5],[1],[5,1]) => returns [1,5]

        1.2 merge_sort([8,3]) => returns [3,8]





        1.3 merge([1,5],[3,8],[5,1,8,3]) => returns [1,3,5,8]



    2. merge_sort([9,10,15,4]) => returns [4,9,10,15]









    3. merge([1,3,5,8],[4,9,10,15],[5,1,8,3,9,10,15,4])



i = 0
j = 0
k = 0

i<4 && j<4
    left[0] <= right[0]
    [1,1,8,3,9,10,15,4]
    k = 1
    i = 1
    j = 0

    left[1] <= right[0]
    [1,3,8,3,9,10,15,4]
    k = 2
    i = 2
    j = 0

    left[2] > right[0]
    [1,3,4,3,9,10,15,4]
    k = 3
    i = 2
    j = 1

    .
    .
    .
    
    i = 5 or j = 5 you stop

"""