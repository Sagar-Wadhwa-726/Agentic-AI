def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

# We are going to get the menu little from the local chai and little from the imported chai

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

# We can also close halway through the point

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order "
    except:
        print("Stall closed, no more chai !")

stall = chai_stall()
print(next(stall))

# Here the generator is waiting for some value but the 
stall.close() # cleanup, we should always close our generators, this will internally call the exit method
# this is used for the cleanup of the memory

# yield can be used to pause and resume the execution of a function
# next() can be used to print the next value from the generator
# send() can be used to send value to the generators
# yield from can be used to yield the values from some other place
# close() can be used to close the generator gracefully, no memory leaks, no program crash