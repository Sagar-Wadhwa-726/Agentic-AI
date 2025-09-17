# Object oriented programming in python

"""A class is a blueprint for the object, where as the objects are the actual instance in the world.
A class can have attributes and the methods. Everything in python is an object - even the class internally is an object itself"""

class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai))

# Creating object of the Chai Class
ginger_tea = Chai()

print(type(ginger_tea))

print(type(ginger_tea) is Chai)
print(type(ginger_tea) is ChaiTime)