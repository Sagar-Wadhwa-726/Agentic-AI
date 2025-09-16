# this can be used to preserve the metadata of the function
from functools import wraps

# Decorators - these are like wrapper functions

# decorators take parameters as the functions

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

# Whatever coming in next line is wrapped up
@my_decorator
def greet():
    print("Hello from decorator module !")

greet()

# The metadata of the fucntion also changes
print(greet.__name__)
