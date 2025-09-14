from fractions import Fraction

# Create a Fraction from integers
f1 = Fraction(1, 3)
print(f"Fraction from integers: {f1}")

# Create a Fraction from a float (be careful with floating-point representation)
f2 = Fraction(0.1) # This will be based on the float's binary representation
print(f"Fraction from float 0.1: {f2}") 

# Better way to create a Fraction from a float's value
f3 = Fraction('0.1') 
print(f"Fraction from string '0.1': {f3}")

# Perform arithmetic operations
result_add = f1 + f3
print(f"1/3 + 1/10 = {result_add}")

result_mul = f1 * f3
print(f"1/3 * 1/10 = {result_mul}")

# Convert a Fraction to a float
float_value = float(result_add)
print(f"Result as a float: {float_value}")