def fizz_buzz_it(n):
    if n%5 == 0 and n%3 == 0:
        return 'fizzbuzz'
    if n%3 == 0:
        return 'fizz'
    if n%5 == 0:
        return 'buzz'
    return n
