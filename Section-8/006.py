# Decorator can be used for logging, to log the entry and exit of a function
# Can be used to check how long a function takes to execute
# Can be used for authentication and authorization purposes
from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"function call started : {func.__name__}")
        result = func(*args, **kwargs)
        print(f"function call ended : {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type, milk="no"):
    print(f"Brewing {type} chai ! and the value for milk is: {milk}")

brew_chai("Masala Chai")
    