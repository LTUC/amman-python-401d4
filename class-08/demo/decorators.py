
def do_twice_decorator(func):
    def _wrapper(*args, **kwargs):
        print('This is called using a decorator')
        func(*args, **kwargs)
        func(*args, **kwargs)
        print('Done with decoration...')
    return _wrapper


@do_twice_decorator
def say_hi():
    print('hi')


@do_twice_decorator
def show_name(name):
    print(f'My name is {name}')

@do_twice_decorator
def show_full_name(f_name, l_name):
    print(f'This is {f_name} {l_name}!')

@do_twice_decorator
def show_info(name='Ahmad', city='Amman', age='25'):
    print(f'My name is {name}, I live in {city}, and Im {age} years old')

if __name__=="__main__":
    say_hi()
    show_name('Ahmad')
    show_full_name('Ahmad', 'Alawad')
    show_info()