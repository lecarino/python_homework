# Task 1: Writing and Testing a Decorator

# one time setup
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs): #Functions may have positional arguments, keyword arguments, both, or neither
        #name
        function_name = func.__name__

        #input params
        pos_params = args if args else "none" #log position params if none then write none
        kw_params = kwargs if kwargs else "none" #log key word params if none then write none

        #the value the function returns. Run the function with arbitrary params and store the return in result
        result = func(*args,**kwargs)

        # To write a log record:
        logger.log(logging.INFO, f'function: {function_name}')
        logger.log(logging.INFO, f'positional parameters: {pos_params}')
        logger.log(logging.INFO, f'keyword parameters: {kw_params}')
        logger.log(logging.INFO, f'return: {result}')
        return result
    return wrapper

# Declare a function that takes no parameters and returns nothing. Maybe it just prints "Hello, World!". Decorate this function with your decorator.
@logger_decorator
def hello():
    print("Hello")

# Declare a function that takes a variable number of positional arguments and returns True. Decorate this function with your decorator.
@logger_decorator
def positional_test(*args):
    return True

# Declare a function that takes no positional arguments and a variable number of keyword arguments, and that returns logger_decorator. Decorate this function with your decorator.
@logger_decorator
def keywords_test(**kwargs):
    return logger_decorator

hello()
positional_test(12,6,1, "Larrenz")
keywords_test(person="Larry", number=12)