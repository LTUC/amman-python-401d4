# Abdullah => one Stack
# Amarah => Array and Regex
# Obada => 3 counts and Regex

import pysnooper

@pysnooper.snoop('./snoop+logs.log')
def check_brackets(text): # text is n length
    stack = [] # as a stack
    brack_dict = {'}':'{', ']':'[', ')':'('}
    for char in text: # O(n)
        # if open
        if char in brack_dict.values(): # Hidden loop O(n) => Always size 3
            stack.append(char)
        # if closed
        if char in brack_dict: # ] => Always size 3
            bracket = stack.pop() # [
            if brack_dict[char] != bracket:
                return False
        #if other, do nothing
    if stack:
        return False
    return True
# O(n^2) but it's really O(3*n)

if __name__=='__main__':
    print(check_brackets('{}{Code}[Fellows](())'))

# To avoid hidden loop:
# a = [3,6,1,9,7]
# if 6 in a: # O(n)
#     print('yes')

# a_as_set = set(a)
# if 6 in a_as_set: # O(1)
#     print('yes')




    # Sol 1 - Obada
    # c1a = 0# find open { and count them
    # c1b = 0# find open } and count them
    # c2a = 0# find open [ and count them
    # c2b = 0# find open ] and count them
    # c3a = 0# find open ( and count them
    # c3b = 0# find open ) and count them
    # compare a with b
    # if passed:
    # Regex to check order of {}
    # \{.?\} find a { and any etxt between them {}{}  {{}}
    # 6 Regex conditions to cover all cases



    # Sol 2 - Amarah
    # chars = [] # as a stack
    # brack_dict = {'{':'}', '[':']', '(':')'}
    # {[hi]} => {[]}
    # Regex re.sub(r'[\w\d\s]', '', text) => {[]}
    # chars = ['{','[',']','}'] 
    # False on odd length
    


    # Sol 3 - Abdullah
    # stack = Stack() or []
    # brack_dict = {'}':'{', ']':'[', ')':'('}
    # Loop
        # if open: push/append to stack
        # if closed: pop the stack, if matches brack_dict[closed_bracket] move on
        # if other char, skip
        # we stop when done with string
    # if array still has chars, return false
    # return True

# Come back at 10:05