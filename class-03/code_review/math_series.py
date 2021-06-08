def fib(n):
    return sum_series(n, 0, 1)



def lucas(n):
    return sum_series(n, 2, 1)

def sum_series(n, a=0, b=1):
    """
    Recursive function that solve a sum series similar to Fibonacci and Lucas

    Arguments:
        n:integer -- the number of sequence we are looking for
        a:optional integer -- value of series at index 0
        b:optional integer -- value of series at index 1

    Returns:
        Number similar to Fibonacci and Lucas series 
        but could be any other math series based on the first two values
    """
    # First base case (a)
    # Second base case (b)
    # Recursive call
    pass

def print_hi():
    print("Hi")


fib(3)
lucas(5)
sum_series(4, 0, 1) == fib(4)     # 0, 1, 1, 2, 3 => 3
sum_series(4, 2, 1) == lucas(4)   # 2, 1, 3, 4, 7 => 7
sum_series(4, 7, 12)              # 7, 12, 19, 31, 50 => 50
sum_series(4)



