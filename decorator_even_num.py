def even_numbers(func):
    """Decorator return even numbers"""
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        result = func(*args, **kwargs)
        if type(result) is str:
            raise TypeError
        else:
            return filter(lambda x: x % 2 == 0, result)
    return wrapper


@even_numbers
def input_numbers(string):
    """Take a string and return a list of int"""
    try:
        return [int(i) for i in string.split()]
    except ValueError:
        return "Invalid input, expected digits"


if __name__ == '__main__':
    try:
        print(list(input_numbers('1 2 3 4 5 5 6   6')))
    except TypeError:
        print("Invalid input, expected digits")
