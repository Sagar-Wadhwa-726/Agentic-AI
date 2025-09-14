# Tuples in python
my_first_tuple = (1, 2, 3, 4, 5)
print(my_first_tuple.count(3)) # Count the occurrences of an element
print(my_first_tuple.index(3)) # Get the index of an element
print(f"My first tuple : {my_first_tuple}")

(num1, num2, num3, num4, num5) = my_first_tuple # Tuple unpacking
print(f"Num1 : {num1}, Num2 : {num2}, Num3 : {num3}, Num4 : {num4}, Num5 : {num5}")

# Membership
print(f"Is 33 in my_first_tuple : {33 in my_first_tuple}")