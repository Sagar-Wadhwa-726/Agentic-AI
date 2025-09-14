# Set and Frozen set in python
# Set is a collection of unordered, mutable and unique elements

# To create a non-empty set
# my_first_set = {1, 2, 3, 4, 5}
# print(my_first_set)

# To create an empty set
# my_second_set = set()
# print(my_second_set)

# Set operations
first = {1,2,3,4,5}
second = {4,5,6,7,8}
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

# Membership test
print(1 in first)
print(11 in first)

# Frozen set is a collection of unordered, immutable and unique elements
# It's just a set but just immutable
my_frozen_set = frozenset({1,2,3,4,5})
print(my_frozen_set)
# my_frozen_set.add(6) # This will raise an error as frozen set is immutable

try:
    my_frozen_set.add(6)
except AttributeError as e:
    print(f"Error: {e}")
