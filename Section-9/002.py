# Classes and the namespaces - each object can have an attribute (property), and the methods (behaviors of the object)

# Each object has it's own features/property - which is known as namespace

# Namespace

class Chai:
    # property
    origin = "India"

print(Chai.origin)

# Not necessary to define all the properties in the class
Chai.is_hot = True
print(Chai.is_hot)

# Creating objects from class Chai
masala = Chai()

print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")

# this proves the point that each object is having it's own namespace and by default if we are changing the properties of an object it won't be reflected for the class properties
masala.is_hot = False

print("Class:", Chai.is_hot)

print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")

# this property does not exist in the class, only with the object "Masala"
masala.flavor = "Masala"
print(masala.flavor)