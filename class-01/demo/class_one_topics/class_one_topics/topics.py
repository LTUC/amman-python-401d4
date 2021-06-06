def input_output():
    """
    This is docstring for input_output function.

    This function shows different ways of printing
    Input: N/A
    Output: Different ways of printing
    """
    fav_color = input('What is your fav color? ')
    name = input('Your name? ')
    age = int(input('How old are you?'))
    print(f'Your fav color is {fav_color} Great choice {name}. You are {age} years old, not bad')
    print('Your fav color is ' + fav_color + ' Great choice ' + name + '. You are ' + str(age) + ' years old, not bad')
    print('Your fav color is {} Great choice {}. You are {} years old, not bad'.format(fav_color, name, age))
    print('Your fav color is %s Great choice %s. You are %d years old, not bad' %(fav_color, name, age))




# Try learning about dedent at home

def get_fav_pet():
    return 'horse'


if __name__ == "__main__": # if running this as a script using $ python topics.py
    print("I'm running this as a script")
    input_output()
    print(get_fav_pet())

# print(__name__)
# dender