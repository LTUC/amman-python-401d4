from factorial_recursion import __version__
from factorial_recursion.factorial import fact

def test_version():
    assert __version__ == '0.1.0'


def test_3():
    assert fact(3) == 6

def test_1():
    assert fact(1) == 1

def test_5():
    assert fact(5) == 5*4*3*2*1







# fact(3) = 3*2*1
# fact(4) = 4*3*2*1
# fact(5) = 5*4*3*2*1

# fact(5) = 5 * fact(4)
#               4 * fact(3)
#                   3 * fact(2)
#                       2 * fact(1)
#                           1

