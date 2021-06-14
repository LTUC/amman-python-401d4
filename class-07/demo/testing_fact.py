

def check(a, b):
    return a>b


def fake_testing():
    print('Hello Im testing things in a wrong place')
    assert check(5,1) == True # pass
    print('Seems like case 1 passed')
    assert check(2,4) == False # pass
    print('All went fine! Congratulations')


fake_testing()


"""
For any test function to be condsiered offical test:
1. Python file should be in tests/ folder
2. Name of function should start with test_
"""