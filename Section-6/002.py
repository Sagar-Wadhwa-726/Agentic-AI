# positional arguments

def add_two_numbers(a,b):
    return a+b

print(add_two_numbers(3,5))

# keyword arguments

def subtract_two_numbers(a,b):
    return a-b

subtract_two_numbers(b=5, a=3)

# *args, **kwargs
# *args refers to variable number of positional arguments
# **kwargs refers to variable number of keyword arguments

def multiply_numbers(*args, **kwargs):
    print(args)
    print(kwargs)
    result = 1
    for num in args:
        result *= num
    for key in kwargs:
        result *= kwargs[key]
    return result

multiply_numbers(1,2,3, num4=4, num5=5)

'''args and kwargs refer to the variable number of positional arguments and kwargs refers to the 
variable number of positional arguments'''
