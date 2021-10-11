import functools

def FuncDecoratorOne(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling: ", func.__name__)
        return func(*args, **kwargs)
    return wrapper


def FuncDecoratorListProperties(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Object's properties: ", args[0].__dict__)
        return func(*args, **kwargs)
    return wrapper


def ClassDecoratorOne(c):
    __init__ = c.__init__
    @functools.wraps(c.__init__)
    def wrapper(_self_, *args, **kwargs):
        __init__(_self_, *args, **kwargs)
    c.__init__ = wrapper
    return c