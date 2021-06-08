def divide(a, b):
    try:
        a = float(a)
        b = float(b)
        print(f'The result of {a}/{b} is {a/b}')
    except ValueError:
        print('Data you entered are not numbers')
    except ZeroDivisionError:
        print('You cant divide by Zero dude')
    except Exception as e:
        print('Something went wrong! Check it out below: ')
        print(e)
    else:
        print('All good!')
    finally:
        print('Thank you for using our app')

def get_input_and_divide():
    a = input('Enter first number: ')
    b = input('Enter second number: ')
    divide(a, b)


if __name__ == '__main__':    
    get_input_and_divide()
