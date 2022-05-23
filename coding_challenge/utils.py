MAX_INPUT_VALUE = 1000


def input_validator(func):

    def wrapper(*args):

        validate_numeric = lambda x: type(x) == int
        is_num = [ validate_numeric(arg) for arg in args[1::] ]
  
        if not all(is_num):
            raise ValueError(f'Please enter only numeric values')

        for arg in args[1::]:
            if not ((arg >= 0) and (arg <= MAX_INPUT_VALUE)):
                raise ValueError(f'The entered number is out of range: {arg}')

        return func(*args)

    return wrapper
