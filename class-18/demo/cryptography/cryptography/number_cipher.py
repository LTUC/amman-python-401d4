def encrypt(number, key):
    """
    Inputs:
    - number to encrypt
    - key for encryption purposes

    Output:
    - encrypted number

    >>> encrypt(1234, 2)
    3456
    >>> encrypt(1234, 5)
    6789

    Special case:
    >>> encrypt(8391, 3)
    1624
    """
    
    number_as_str = str(number) # '1234'
    result = ''
    for digit in number_as_str:
        shifted_digit = (int(digit) + key) % 10
        result += str(shifted_digit)
    
    return int(result)


def decrypt(number, key):
    """
    >>> decrypt(6789, 5)
    1234
    >>> decrypt(1624, 3)
    8391
    """
    return encrypt(number, -key)


if __name__=='__main__':
    assert encrypt(1234, 2) == 3456
    assert encrypt(1234, 5) == 6789
    assert encrypt(8391, 3) == 1624
    assert decrypt(6789, 5) == 1234
    assert decrypt(1624, 3) == 8391
    print('All tests passed')

