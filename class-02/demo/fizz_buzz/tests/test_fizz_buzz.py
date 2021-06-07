from fizz_buzz import __version__
from fizz_buzz.check_fizz_buzz import fizz_buzz_it

def test_version():
    assert __version__ == '0.1.0'

def test_six():
    assert fizz_buzz_it(6) == 'fizz'

def test_ten():
    assert fizz_buzz_it(10) == 'buzz'

def test_thirty():
    expected = 'fizzbuzz'
    actual = fizz_buzz_it(30)
    assert expected == actual

def test_seven():
    expected = 7
    actual = fizz_buzz_it(7)
    assert expected == actual


def test_full_array():
    a = [1,2,3,4,5,6,7,8,9,15]
    expected = [1,2,'fizz',4,'buzz','fizz',7,8,'fizz','fizzbuzz']
    for i in range(len(a)):
        assert fizz_buzz_it(a[i]) == expected[i]