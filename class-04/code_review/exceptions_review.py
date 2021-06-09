def math_process(x,y):
    try:
        result = x/y * (3+x) / (4)
        if result < 0:
            raise Exception
    except ZeroDivisionError:
        return "You can't divide by zero"
    except Exception:
        return "Something went wrong with the result"


if __name__ == "__main__":
    print(math_process(-2, 5))