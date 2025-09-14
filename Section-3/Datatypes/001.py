# Values are immutable in python
# Always check immutability or mutability of an object through id() function
# Immutable datatypes: int, float, bool, string, tuple
# Mutable datatypes: list, dict, set

sugar_amount = 2
print(f"Initial sugar : {sugar_amount}")

sugar_amount = 12
print(f"Second Initial sugar : {sugar_amount}")


# In Python integers are immutable, so when we change the value of sugar_amount,
# a new object is created in memory and the reference of sugar_amount is changed to point to the new object.
# The old object will be destroyed by the garbage collector if there are no more references to it

# Don't check the immutability or mutability of an object through the values, check through ID
print(f"The id of 2 is : {id(2)}")
print(f"The id of 12 is : {id(12)}")

# Set - A collection of unique items, unordered, mutable
spice_mix = set()
spice_mix.add("cumin")
print(f"Initial spice mix : {spice_mix}")
print(f"The id of spice mix is : {id(spice_mix)}")

spice_mix.add("turmeric")
print(f"Second spice mix : {spice_mix}")
print(f"The id of spice mix is : {id(spice_mix)}")