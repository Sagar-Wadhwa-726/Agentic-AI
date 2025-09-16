# Generator - Generating thing
# In loops everything gets loaded in the memory
# From generator we get one value at a time - it's optimized in certain cases
# We don't get the results immediately from Generator
# Lazy evaluation

# Generator function
def serve_chai_gen():
    yield "Cup-1 : Masala Chai"
    yield "Cup-2 : Ginger Chai"
    yield "Cup-3 : Elaichi Chai"

# Normal function
def get_chai_list():
    return ["Cup-1", "Cup-2", "Cup-3"]


stall = serve_chai_gen()

"""This is just a generator object, stall is just referencing to the method, actual values will be provided as and when needed"""
print(stall)

"""If we want the actual values, we can get the first value using next method, this will provide us with the first yield value, and a track will be kept where the function was paused last time"""
print(next(stall))
print(next(stall))
print(next(stall))

"""This will throw error because there is nothing more to be yielded from the function"""
# print(next(stall))

"""Generators are particularly useful for opening a connection or closing the connection to the database"""

